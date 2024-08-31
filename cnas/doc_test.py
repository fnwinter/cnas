#!/bin/python3

import os
import doctest


def run_doctests_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Running doctest for {file_path}")
                doctest.testfile(file_path, module_relative=False)


if __name__ == "__main__":
    _directory = os.path.abspath(os.path.dirname(__file__))
    run_doctests_in_directory(_directory)
