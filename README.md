# bluefin and aurora

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2503a44c1105456483517f793af75ee7)](https://app.codacy.com/gh/ublue-os/bluefin/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

[![GTS Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-gts.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-gts.yml)[![Stable Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-stable.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-stable.yml)[![Latest Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-latest.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-latest.yml)[![Beta Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-beta.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-beta.yml)

## Bluefin - [projectbluefin.io](https://projectbluefin.io)

![image](https://github.com/ublue-os/bluefin/assets/1264109/b093bdec-40dc-48d2-b8ff-fcf0df390e8c)

> "Evolution is a process of constant branching and expansion." - Stephen Jay Gould

Bluefin strives to cover these two use cases. For end users it provides a system as reliable as a Chromebook with near-zero maintainance, with the power of homebrew, flathub, and a container runtime to give you access to all the best software Open Source has to offer. Check [Introduction to Bluefin](https://universal-blue.discourse.group/t/introduction-to-bluefin/41) for a feature walkthrough.

- [Download Bluefin](https://projectbluefin.io/#scene-picker)

## Aurora - [getaurora.dev](https://getaurora.dev)

![Screenshot_20240423_211805](https://github.com/ublue-os/bluefin/assets/40402114/1bea1ed8-d97a-402a-957b-e0f338d38230)

Aurora is a delightful KDE desktop experience for end-users that are looking for reliability and developers for the most-hassle free setup. Zero maintenance included.

- [Download Aurora](https://getaurora.dev)

### What's the relationship between Aurora and Bluefin?

Both Aurora and Bluefin strive to offer a curated out of the box experience for users, they only differ in the default desktop and recommended applications: Bluefin uses GNOME, Aurora uses KDE. They are both maintained and built in this repository.

## Documentation

1. [Discussions and Announcements](https://universal-blue.discourse.group/c/bluefin/6) - strongly recommended!
2. [Documentation](https://docs.projectbluefin.io/)
3. [Contributing Guide](https://docs.projectbluefin.io/contributing)

### Secure Boot

Secure Boot is supported by default on our systems, providing an additional layer of security. After the first installation, you will be prompted to enroll the secure boot key in the BIOS.

Enter the password `universalblue`
when prompted to enroll our key.

If this step is not completed during the initial setup, you can manually enroll the key by running the following command in the terminal:

`
ujust enroll-secure-boot-key
`

Secure boot is supported with our custom key. The pub key can be found in the root of the akmods repository [here](https://github.com/ublue-os/akmods/raw/main/certs/public_key.der).
If you'd like to enroll this key prior to installation or rebase, download the key and run the following:

```bash
sudo mokutil --timeout -1
sudo mokutil --import public_key.der
```

## Repobeats

![Alt](https://repobeats.axiom.co/api/embed/40b85b252bf6ea25eb90539d1adcea013ccae69a.svg "Repobeats analytics image")

## Star History

<a href="https://star-history.com/#ublue-os/bluefin&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ublue-os/bluefin&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ublue-os/bluefin&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ublue-os/bluefin&type=Date" />
  </picture>
</a>
