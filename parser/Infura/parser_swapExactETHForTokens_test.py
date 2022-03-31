import json
from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0xbe80c945579b5a4463ad755f6ae490665e9c16d6f26f0eb377a4acc6e179a1ab",
        "url": "https://etherscan.io/tx/0xbe80c945579b5a4463ad755f6ae490665e9c16d6f26f0eb377a4acc6e179a1ab",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2021-04-13T08:22:22+00:00",
        "in_amount": "76942.778800938569978049",
        "in_amount_major": "140.0",
        "in_currency": "BUSD",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "140.0",
        "out_amount_major": "140.0",
        "out_currency": "BNB",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.00056885",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    Infura_parser_lookup.update_major_currency("BNB")
    result = prepare_parse_result(__file__)
    Infura_parser_lookup.update_major_currency("Ether")  # patch back

    assert len(result) == 1

    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
