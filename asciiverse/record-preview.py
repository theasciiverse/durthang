#!/usr/bin/env python3
"""Records asciiverse/durthang.cast, Durthang's catalog preview, at 100x30
(hub/RECORDING.md): the server list with BatMUD (asciiverse/preview-config.toml),
then a TLS connection showing BatMUD's greeting. The character has no login,
so nothing is ever sent but the connection itself. Usage, from the repo root
with a release build in target/release:
    python3 asciiverse/record-preview.py"""
import os, pty, shutil, struct, fcntl, select, tempfile, termios, time

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
home = tempfile.mkdtemp()
os.makedirs(f"{home}/.config/durthang")
shutil.copy(f"{root}/asciiverse/preview-config.toml", f"{home}/.config/durthang/config.toml")
env = dict(os.environ, HOME=home, XDG_CONFIG_HOME=f"{home}/.config", TERM="xterm-256color",
           COLORTERM="truecolor", LANG="C.UTF-8")
DOWN, ENTER = b"\x1b[B", b"\r"
keys = [(3.0, DOWN), (1.2, DOWN), (2.0, ENTER), (12.0, b"\x11"), (1.0, b"q"), (1.0, b"")]

pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", f"{root}/target/release/durthang",
        f"{root}/asciiverse/durthang.cast"], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))
for wait, key in keys:
    end = time.time() + wait
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.1)
        if r:
            try: os.read(fd, 65536)
            except OSError: break
    if key: os.write(fd, key)
os.waitpid(pid, 0)
shutil.rmtree(home)
