from unittest import TestCase

from models.exceptions import TransactionSkipped
from parser.Infura.util import prepare_parse_result


def test() -> None:
    TestCase().assertRaises(TransactionSkipped, lambda: prepare_parse_result(__file__))
