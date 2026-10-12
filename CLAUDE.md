# Durthang (Asciiverse packaging)

A terminal MUD client in Rust and Ratatui by Raimo Geisel, packaged for the
Asciiverse catalog (kind `program`, topic `mud-client`) and as system
packages. Not our code: keep changes small, list every one in PATCHES.md,
and offer fixes upstream.

- Remotes: `upstream` is github.com/Pommersche92/durthang, `origin` is
  github.com/theasciiverse/durthang (public, because the GPL asks that the
  source of what we ship is available).
- Branch `asciiverse` = an upstream release tag plus our commits.
- Release: tag `v<upstream version>-av.<n>` and push it; the workflow builds
  everything and attaches it to a GitHub release.
- Local static build: `docker run --rm -v "$PWD":/src -w /src rust:1-alpine
  sh -c 'apk add musl-dev pkgconf perl make && cargo build --release'`.
- Durthang takes no host or port on its command line (only `--config`), so
  av can install and launch it but cannot open a world in it directly.
