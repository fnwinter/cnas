#!/bin/python3

import os
import sys
import subprocess


def run_pylint_on_directory(directory: str):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Running pylint on {file_path}")
                try:
                    subprocess.run(['pylint', file_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"error while pylint {str(e)}")


def fix_autopep8_on_directory(directory: str):
    print(f"Fixing pylint on {directory}")
    try:
        subprocess.run(['autopep8', '--in-place',
                        '--aggressive', '--recursive', directory], check=True)
    except subprocess.CalledProcessError as e:
        print(f"error while fixing pylint {str(e)}")


if __name__ == "__main__":
    _directory = os.path.abspath(os.path.dirname(__file__))

    if len(sys.argv) > 1 and sys.argv[1] == '--fix':
        fix_autopep8_on_directory(_directory)
    else:
        run_pylint_on_directory(_directory)
