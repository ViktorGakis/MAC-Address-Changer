from collections import namedtuple
from unittest.mock import patch

import pytest

from machanger.config import Config

# Create a mock version_info named tuple
MockVersionInfo = namedtuple(
    "version_info", ["major", "minor", "micro", "releaselevel", "serial"]
)


@pytest.fixture
def config() -> Config:
    return Config()


@pytest.fixture
def mock_python2_env():
    with patch("sys.version_info", new=MockVersionInfo(2, 7, 0, "final", 0)):
        yield


@pytest.fixture
def mock_python3_env():
    with patch("sys.version_info", new=MockVersionInfo(3, 8, 0, "final", 0)):
        yield
