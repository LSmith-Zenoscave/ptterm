#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

requirements = [
    'prompt_toolkit>=3.0.0,<3.1.0',
    'pyte>=0.5.1',
]

# Install yawinpty on Windows only.
if sys.platform.startswith('win'):
    requirements.append('yawinpty')


setup(
    name='ptterm',
    author='Jonathan Slenders',
    version='0.1',
    license='LICENSE',
    url='https://github.com/prompt-toolkit/ptterm',
    description='Terminal emulator for prompt_toolkit.',
    long_description=long_description,
    packages=find_packages('.'),
    install_requires = requirements,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python",
    ],
)
