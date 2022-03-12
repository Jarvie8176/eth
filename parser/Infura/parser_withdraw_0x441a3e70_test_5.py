from unittest import TestCase

from models.exceptions import TransactionSkipped
from parser.Infura.util import prepare_parse_result


def test() -> None:
    # https://bscscan.com/tx/0x1891dc80605b4cd3838bfe43a78924bdc3bec1abe801e85815f4ed8b8bfafdaa
    TestCase().assertRaises(TransactionSkipped, lambda: prepare_parse_result(__file__))
