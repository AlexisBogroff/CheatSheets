# Minimalistic Procedure
_from https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html_

Requires setuptools and wheels packages

## What your package should contain

Package structure
```
package_name/
    setup.py
    package_name/
          __init__.py
          module1.py
```

The added file setup.py enables the build
``` python
from setuptools import setup

setup(
  name='package_name',
  version='0.1.0',
  packages=['package_name'],
)
```

## Commands to make the build

Create the source distribution
``` python
python setup.py sdist
```
Build the distribution wheel
``` python
python setup.py bdist_wheel
```
Build the package
``` python
python setup.py build
```

## Install the package

Static mode: if you modify the package, you need to reinstall
``` python
python setup.py install
```

Dynamic mode: each new import will get the latest version
``` python
python setup.py develop
```
