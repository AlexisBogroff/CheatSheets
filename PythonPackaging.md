# Minimalistic Procedure
_Requires setuptools_

## Create file:
setup.cfg

### Containing:
[metadata]

name = <name_package>


## Create file:
setup.py

### Containing:
from setuptools import setup

setup()


## Make the build:
python setup.py sdist

## Install the package:
pip install <name_package>
