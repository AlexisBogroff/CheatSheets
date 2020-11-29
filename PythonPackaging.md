# Minimalistic Procedure
_Requires setuptools and wheels packages_

## Package structure
```
package_name/
    setup.py
    package_name/
          __init__.py
          module1.py
```

## Create file
setup.py

``` python
from setuptools import setup

setup(
  name='package_name',
  version='0.1.0',
  packages=['package_name'],
)
```

## Make the build
### Create the source distribution
``` python
python setup.py sdist
```
### Build the distribution wheel
``` python
python setup.py bdist_wheel
```
### Build the package
``` python
python setup.py build
```

## Install the package:
``` python
python setup.py install
```