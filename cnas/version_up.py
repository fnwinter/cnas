#!/bin/python3
import os
import subprocess

VERSION = "0.0.17"


def increase_version():
    version_parts = VERSION.split(".")
    version_parts[-1] = str(int(version_parts[-1]) + 1)
    return ".".join(version_parts)


def make_commit():
    execute_command("git add --all")
    execute_command(f"git commit -m \"update version {VERSION}\"")
    execute_command("git push origin main")


def execute_command(command):
    try:
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"error while fixing pylint {str(e)}")


if __name__ == "__main__":
    script_absolute_path = os.path.abspath(__file__)
    with open(script_absolute_path, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        lines[4] = f"VERSION = \"{increase_version()}\"\n"
        f.write("".join(lines))
    make_commit()
