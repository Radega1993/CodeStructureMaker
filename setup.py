#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='CodeStructureMaker_v1',
    version='1.0',
    description='Software to generade structures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Raül de Arriba',
    author_email='rauldearriba@gmail.com',
    url='https://github.com/Radega1993/CodeStructureMaker',
    packages=setuptools.find_packages(),
    setup_requires=['wheel'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
