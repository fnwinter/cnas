#!/usr/bin/python3
# Copyright 2024 fnwinter@gmail.com

from setuptools import setup, find_packages
from cnas.version_up import VERSION

def read_package():
    with open("cnas/requirements.txt") as f:
        lines = [item.strip() for item in f.readlines()]
        return lines

setup(name='cherrynas',
      version=VERSION,

      url='https://github.com/fnwinter/cnas',
      author='JungJik Lee',
      author_email='fnwinter@gmail.com',

      description='Installable NAS software',
      long_description='',

      packages=find_packages(),
      package_dir={'cherrynas': 'cnas'},

      zip_safe=False,
      install_requires=read_package(),
      include_package_data=True
      )
