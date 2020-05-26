#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='codestructuremaker',
    version='1.0',
    description='Software to generade structures',
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Raül de Arriba',
    author_email='rauldearriba@gmail.com',
    url='https://github.com/Radega1993/CodeStructureMaker',
    packages=find_packages(),
    python_requires='>=3.6',
    scripts=["app.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
