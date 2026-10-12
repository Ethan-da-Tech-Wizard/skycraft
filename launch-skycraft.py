#!/usr/bin/env python3
"""Start SkyCraft and its Windows Minecraft launcher in the same Proton prefix."""

import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time


BASE = Path(__file__).resolve().parent
STATE = json.loads((BASE / "installation-manifest.json").read_text())
GAME = Path(STATE["game"])
PREFIX = Path(STATE["launch_prefix"])
STEAM = Path.home() / ".local/share/Steam"
LIBRARY = GAME.parent.parent
PROTON = LIBRARY / "common/Proton - Experimental/proton"
PRISM = PREFIX / "drive_c/users/steamuser/AppData/Local/SkyCraft/Prism/prismlauncher.exe"
SKSE = GAME / "skse64_loader.exe"
ADDRESS_LIBRARY = GAME / "Data/SKSE/Plugins/versionlib-1-7-104-0.bin"


def requirements(minecraft_only=False):
    items = [("Proton", PROTON), ("Minecraft launcher", PRISM)]
    if not minecraft_only:
        items += [
            ("Skyrim", GAME / "SkyrimSE.exe"),
            ("SKSE mod loader", SKSE),
            ("SKSE for Skyrim 1.7.104", GAME / "skse64_1_7_104.dll"),
            ("Address Library for Skyrim 1.7.104", ADDRESS_LIBRARY),
            ("SkyCraft mod", GAME / "Data/SKSE/Plugins/SkyCraft.dll"),
        ]
    return items


def show_error(message):
    print(message, file=sys.stderr)
    if shutil.which("zenity") and (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
        subprocess.Popen(
            ["zenity", "--error", "--title=SkyCraft", "--no-markup", "--text=" + message],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minecraft", action="store_true", help="Open the Minecraft launcher for sign-in or settings")
    parser.add_argument("--check", action="store_true", help="Check required files without starting anything")
    args = parser.parse_args()
    items = requirements(args.minecraft)
    missing = [label for label, path in items if not path.is_file()]
    if args.check:
        for label, path in items:
            print(f"{label}: {'ready' if path.is_file() else 'MISSING'}")
        print(f"SkyCraft game profile: {PREFIX}")
        return 1 if missing else 0
    if missing:
        show_error(
            "SkyCraft setup is not finished. These required files are missing:\n\n"
            + "\n".join(missing)
            + "\n\nFinish installing the matching SKSE and Address Library downloads, then open SkyCraft again."
        )
        return 1

    logs = BASE / "logs"
    logs.mkdir(exist_ok=True)
    if not args.minecraft and subprocess.run(
        ["pgrep", "-x", "steam"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    ).returncode:
        with (logs / "steam-launch.log").open("a") as log:
            subprocess.Popen(
                ["steam", "-silent"], stdin=subprocess.DEVNULL, stdout=log,
                stderr=subprocess.STDOUT, start_new_session=True,
            )
        time.sleep(10)

    env = os.environ.copy()
    env.update({
        "STEAM_COMPAT_DATA_PATH": str(PREFIX.parent),
        "STEAM_COMPAT_CLIENT_INSTALL_PATH": str(STEAM),
        "STEAM_COMPAT_INSTALL_PATH": str(GAME),
        "STEAM_COMPAT_LIBRARY_PATHS": str(LIBRARY),
        "STEAM_COMPAT_APP_ID": "489830",
        "SteamAppId": "489830",
        "SteamGameId": "489830",
    })
    program = PRISM if args.minecraft else SKSE
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_path = logs / f"{'minecraft' if args.minecraft else 'skycraft'}-{stamp}.log"
    with log_path.open("w") as log:
        process = subprocess.Popen(
            [str(PROTON), "run", str(program)],
            cwd=str(program.parent), env=env, stdin=subprocess.DEVNULL,
            stdout=log, stderr=subprocess.STDOUT, start_new_session=True,
        )
    print(f"Started {program.name} (process {process.pid}). Log: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
