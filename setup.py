#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=8.0.0',
    'requests>=2.26.0',
    'pyyaml'
]

setup(
    name='segapi',
    version='0.1.0',
    description="CLI tool segment config api",
    long_description=readme,
    author="Brett Hale",
    author_email='bhale@du.edu',
    packages=find_packages(),
    entry_points={
        # ATTENTION! ACHTUNG! ATENCIÓN!
        #
        # The following lines determine what your CLI program is
        # called and where it will look for it. Please edit to suit
        # your needs
        'console_scripts': [
            'segapi=cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ]
)