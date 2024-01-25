from io import StringIO
from unittest.mock import patch

import pytest

from machanger.argparser import ArgParser, CompatibleArgParser


def test_argparser_python2(mock_python2_env) -> None:
    parser = CompatibleArgParser()
    assert hasattr(parser.parser, "add_option")


def test_argparser_python3(mock_python3_env) -> None:
    parser = CompatibleArgParser()
    assert hasattr(parser.parser, "add_argument")


def help_argument(environment) -> None:
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        with pytest.raises(SystemExit) as e:
            parser = ArgParser()
            parser.add_options()
            parser.parse_args(["--help"])

        assert e.type == SystemExit
        assert e.value.code == 0
        help_output = mock_stdout.getvalue()
        assert "Interface to have its MAC address changed" in help_output


def test_help_argument2(mock_python2_env) -> None:
    help_argument(mock_python2_env)


def test_help_argument3(mock_python3_env) -> None:
    help_argument(mock_python3_env)
