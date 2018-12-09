#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()


info = sys.version_info

setup(
    name='py_kaomoji',
    version='0.1.3.3',
    description='This is a Kaomoji library for Python for Japanese.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Shibui Yusuke',
    author_email='shibuiyusuke@gmail.com',
    url='https://github.com/shibuiwilliam/py-kaomoji',
    packages=find_packages(),
    include_package_data=True,
    keywords='kaomoji',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['kao=kaomoji.kaomoji:main'],
    },
    test_suite="test",
)
