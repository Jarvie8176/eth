import json
from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result
from parser.parserLookup import ParserLookup


def test() -> None:
    expected = {
        "trx_id": "0x7d55734a63e442ad44abdfa70aa59502f670b0f3021dadae58ffc843ccc4589d",
        "url": "https://etherscan.io/tx/0x7d55734a63e442ad44abdfa70aa59502f670b0f3021dadae58ffc843ccc4589d",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2021-04-08T20:41:31+00:00",
        "in_amount": "38939.308604754272208691",
        "in_amount_major": None,
        "in_currency": "USDC",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "59.431604998237528485",
        "out_amount_major": None,
        "out_currency": "mTSLA",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.001074295",
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
