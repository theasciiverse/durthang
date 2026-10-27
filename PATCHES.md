# Changes from upstream

This is the Asciiverse packaging of [Durthang](https://github.com/Pommersche92/durthang)
by Raimo Geisel (GPL-3.0-only), built from upstream's v0.2.0 tag. Upstream
is the `upstream` remote; the `asciiverse` branch carries the changes below.

## Code

- **Cargo.toml: keyring features `apple-native`, `windows-native` and
  `vendored`.** keyring 3 has no default credential store: a platform whose
  store feature is not enabled falls back to the in-memory mock store (see
  keyring's README). v0.2.0 enables only the Linux stores, so on macOS and
  Windows saved passwords did not survive a restart, although the README
  says they go to the Keychain and the Credential Manager. `vendored` builds
  libdbus into the binary, so the static Linux build needs no libdbus on the
  player's machine. Worth sending upstream.

## Packaging (new files, no upstream code touched)

- `.github/workflows/release.yml`: av archives for six targets plus
  SHA256SUMS, and .deb, .rpm, .apk and Arch packages for Linux.
- `asciiverse/nfpm.yaml`: the system package definition.

## Known differences in the builds

- Windows builds use MSVC. Upstream's build.rs embeds the icon with MinGW's
  windres, which MSVC builds skip with a warning, so the exe has no icon.

## Ours

- **How to play it, at the top of README.md.** A short note on installing and
  starting it with av, or from a release archive; the original text follows
  unchanged.
