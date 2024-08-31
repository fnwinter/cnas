#!/bin/python3

import os
import subprocess

def run_pylint_on_directory(directory: str):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Running pylint on {file_path}")
                subprocess.run(['pylint', file_path])

if __name__ == "__main__":
  directory = os.path.abspath(os.path.dirname(__file__))
  run_pylint_on_directory(directory)
