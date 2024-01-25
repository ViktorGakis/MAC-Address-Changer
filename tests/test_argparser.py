from machanger.argparser import CompatibleArgParser


def test_argparser_python2(mock_python2_env) -> None:
    parser = CompatibleArgParser()
    assert hasattr(parser.parser, "add_option")


def test_argparser_python3(mock_python3_env) -> None:
    parser = CompatibleArgParser()
    assert hasattr(parser.parser, "add_argument")
