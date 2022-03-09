import json
from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result
from parser.parserLookup import ParserLookup


def test() -> None:
    expected = {
        "trx_id": "0x3f5cda8c4fa07bdb1d7e72b3759fe072b783e69d2e3da176e770555b70dd3825",
        "url": "https://etherscan.io/tx/0x3f5cda8c4fa07bdb1d7e72b3759fe072b783e69d2e3da176e770555b70dd3825",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2021-02-24T06:04:46+00:00",
        "in_amount": "1.0",
        "in_amount_major": "1.0",
        "in_currency": "BNB",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "247.962994491268382336",
        "out_amount_major": "1.0",
        "out_currency": "USDC",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.00185016",
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
