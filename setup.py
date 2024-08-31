#!/usr/bin/python3
# Copyright 2024 fnwinter@gmail.com

#from cnas import req
from setuptools import setup, find_packages

#VERSION = open("./cnas/version.txt").readline()

setup(name='cherrynas',
      version="1.0.1",

      url='https://github.com/fnwinter/cnas',
      author='JungJik Lee',
      author_email='fnwinter@gmail.com',

      description='Installable NAS software',
      long_description='',

      packages=find_packages(),
      package_dir={'cherrynas': 'cnas'},

      zip_safe=False,
      #install_requires=req,
      include_package_data=True
      )
