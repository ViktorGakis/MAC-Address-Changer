from io import StringIO
from unittest.mock import patch

import pytest

from machanger.argparser import ArgParser


def help_argument(environment, config) -> None:
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        with pytest.raises(SystemExit) as e:
            parser = ArgParser()
            parser.add_options()
            parser.parse_args(["--help"])

        assert e.type == SystemExit
        assert e.value.code == 0
        help_output = mock_stdout.getvalue()
        help_strings = [opt.get("kwds").get("help") for opt in config.parser_options]

        assert all(help_string in help_output for help_string in help_strings)


def test_help_argument2(mock_python2_env, config) -> None:
    help_argument(mock_python2_env, config)


def test_help_argument3(mock_python3_env, config) -> None:
    help_argument(mock_python3_env, config)
