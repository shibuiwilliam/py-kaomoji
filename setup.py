#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()


info = sys.version_info

setup(
    name='kaomoji',
    version='0.1',
    description='Python Boilerplate contains all the boilerplate you need to create a Python package.',
    long_description=readme,
    author='Shibui Yusuke',
    author_email='shibuiyusuke@gmail.com',
    url='https://github.com/shibuiwilliam/py-kaomoji',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords='kaomoji',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test="test",
)
