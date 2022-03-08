from unittest import TestCase

from models.exceptions import ParserNotFound
from parser.Infura.util import prepare_parse_result


def test() -> None:
    TestCase().assertRaises(ParserNotFound, lambda: prepare_parse_result(__file__))
