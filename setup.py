#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='codestructuremaker',
    version='1.0',
    description='Software to generade structures',
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Raul de Arriba',
    author_email='rauldearriba@gmail.com',
    url='https://github.com/Radega1993/CodeStructureMaker',
    packages=find_packages(),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'codestructuremaker = codestructuremaker.app:codestructuremaker_main',
        ],
    },
    package_data={
        'codestructuremaker': [
            'common/*.py',
            'languages/*.py',
            'config/*.py',
            'sample_files/*.py',
            'sample_files/gitignore/*.py'
        ]
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
