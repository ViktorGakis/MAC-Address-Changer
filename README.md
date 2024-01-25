# MAC

- M(edia) A(ccess) C(ontrol)
  - Permanent
  - Physical
  - Unique
- Assigned by manufacturer

The MAC address is used in the network in order to transfer data as a unique identifier.

Why change the MAC Address?

- Increase anonymity
- Impersonate other devices (man in the middle)
- Bypass filters specific to devices

# Developing the application

## ArgParser

We used dependency injection to properly define our arg parser class

```python
class CompatibleArgParser:
    '''Handles the arg parsing along with python version'''
    def __init__(self):
      '''Checks the python version of the system and imports the proper arg parsers'''

    def add_option(self, *args, **kwargs):
      '''decides to use .add_argument or .add_options depending on the python version'''


    def parse_args(self):
      '''decides to use .parse_args or .parse_args()[0] depending on the python version'''      



class ArgParser:
    '''final arg parser class with sanitized commands'''
    def __init__(self):
        self.parser = CompatibleArgParser()

    def add_options(self):
        self.parser.add_option("-i", "--interface", dest="interface", help="Interface to have its MAC address changed", required=True)

    def parse_args(self):
        return self.parser.parse_args()
```

## Testing

To test the package the recommended method is to install it in development mode. Assuming that there exists the setup.py file as in our case

```python
pip install -e .
```

### Note on Python System Version Mocking

Mocking the system version is enabled by using the mock functionality of pytest and mimicking the type of the sys.version_info which is a namedtuple as follows

```python
from unittest.mock import patch
from collections import namedtuple

MockVersionInfo = namedtuple('version_info', ['major', 'minor', 'micro', 'releaselevel', 'serial'])

with patch('sys.version_info', new=MockVersionInfo(2, 7, 0, 'final', 0)):
  # whatever follows asumes 
```
