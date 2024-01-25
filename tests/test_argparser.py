import sys
from unittest.mock import patch
from machanger.argparser import ArgParser
from collections import namedtuple

# Create a mock version_info named tuple
MockVersionInfo = namedtuple('version_info', ['major', 'minor', 'micro', 'releaselevel', 'serial'])

def test_argparser_python2():
    # Mock sys.version_info to simulate Python 2.x
    with patch('sys.version_info', new=MockVersionInfo(2, 7, 0, 'final', 0)):
        parser = ArgParser()
        parser.add_options()
        with patch('sys.argv', ['script_name', '-i', 'eth0']):
            options, _ = parser.parse_args()
            assert options.interface == 'eth0'


def test_argparser_python3():
    # Mock sys.version_info to simulate Python 3.x
    with patch('sys.version_info', new=MockVersionInfo(3, 8, 0, 'final', 0)):
        parser = ArgParser()
        parser.add_options()
        with patch('sys.argv', ['script_name', '-i', 'eth0']):
            args = parser.parse_args()
            assert args.interface == 'eth0'


