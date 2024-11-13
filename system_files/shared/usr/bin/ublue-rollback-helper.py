#!/usr/bin/python3

import json
import re
import subprocess
import sys

TAG_PATTERN = lambda tag: re.compile(rf"{tag}-[0-9]+")

with open('/usr/share/ublue-os/image-info.json') as f:
    image_info = json.load(f)

image_name = image_info["image-name"]
image_tag = image_info["image-tag"]
image_vendor = image_info["image-vendor"]
try:
    valid_streams = image_info["valid-streams"]
except:
    valid_streams = ["stable", "stable-daily", "latest"]



def get_tags(image_name, image_tag, image_vendor) -> list:
    registry = "docker://ghcr.io/" + image_vendor + "/"
    output = subprocess.run(
        ["/usr/bin/skopeo", "inspect", registry + image_name + ":" + image_tag],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    manifest = json.loads(output)
    tags = set()
    for tag in manifest["RepoTags"]:
        if tag.endswith(".0"):
            continue
        if re.match(TAG_PATTERN(image_tag), tag):
            tag = re.sub(rf"{image_tag}-", "", tag)
            tags.add(tag)
    tags = sorted(tags, reverse=True)
    if len(tags) > 31:
        tags = tags[:31]
    return tags

# def rebase(rebase_target):

def rebase_helper(image_name: str) -> bool:
    streams = valid_streams
    choose_target = subprocess.run(
        ["/usr/bin/gum", "choose", "cancel", "date", *streams, "custom"],
        check=True,
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    rebase_target = "ghcr.io/" + image_vendor + "/" + image_name + ":"
    subprocess.run(["clear", "-x"])

    if choose_target == "cancel":
        return False
    elif choose_target == "date":
        print("This will pin you to a specific date",
            "you will need to rebase to update")
        date_tags = get_tags(image_name, image_tag, image_vendor)
        target_tag = image_tag + "-" + subprocess.run(
            ["/usr/bin/gum", "choose", "cancel", *date_tags],
            check=True,
            stdout=subprocess.PIPE,
            text=True
        ).stdout
        if target_tag == "cancel":
            return False
        else:
            rebase_target += target_tag
    elif choose_target == "custom":
        rebase_target = subprocess.run(
            ["/usr/bin/gum", "input", "--placeholder='Custom Target to Rebase to..."],
            check=True,
            stdout=subprocess.PIPE,
            text=True
        ).stdout
        rebase_target = rebase_target[:-1]
        try:
            print("Checking if Valid Target...")
            check = subprocess.run(
                ["/usr/bin/skopeo", "inspect", "docker://" + rebase_target],
                stdout=subprocess.PIPE,
                check=True
            ).returncode
        except:
            print("Not a valid Custom Target")
            return False
    else:
        rebase_target += choose_target

    print(f"You have the following rebase target: {rebase_target}")
    print("Are you sure you want to rebase to that target?")
    if subprocess.run(["/usr/bin/gum", "confirm"], stdout=subprocess.PIPE,
        text=True).returncode == 0:
        print("True")
        return True
    return False

def commandline():
    if sys.argv[1].lower() == "rollback":
        print("rollback")
    elif sys.argv[1].lower() == "rebase":
        print("rebase")
    sys.argv.pop()
    main()

def main():
    if len(sys.argv) > 1:
        commandline()

    subprocess.run(["clear", "-x"])
    print("Choose your action.")
    option = subprocess.run(
        ["/usr/bin/gum", "choose", "exit", "rebase", "rollback"],
        check=True,
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    if "rebase" in option:
        x = rebase_helper(image_name)
        while not x:
            main()
    else:
        subprocess.run(["clear", "-x"])
        exit(0)

if __name__ == "__main__":
    main()
