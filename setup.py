#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=[
        'hyper>=0.7',
    ],
)
