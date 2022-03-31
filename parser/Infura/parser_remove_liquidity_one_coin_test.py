import json
from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0xacd85c207c42c66b3bc9ac3fee3ab5cf1f97f6444b1239e7c76341e856bc9ce3",
        "url": "https://etherscan.io/tx/0xacd85c207c42c66b3bc9ac3fee3ab5cf1f97f6444b1239e7c76341e856bc9ce3",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2021-03-24T22:35:31+00:00",
        "in_amount": "81203.797622459107246478",
        "in_amount_major": None,
        "in_currency": "BUSD",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.000996237",
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
