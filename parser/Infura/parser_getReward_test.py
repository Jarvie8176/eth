import json
from unittest import TestCase

from parser.Infura.defn_parser import Infura_parser_lookup
from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = {
        "trx_id": "0x89dedd4ed2e45b81e65828c6c4ebacc794ec784ba7def425d3396b83af9d2e4d",
        "url": "https://etherscan.io/tx/0x89dedd4ed2e45b81e65828c6c4ebacc794ec784ba7def425d3396b83af9d2e4d",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2021-04-12T09:03:36+00:00",
        "in_amount": "0.158125236436375775",
        "in_amount_major": None,
        "in_currency": "KEY",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.000452975",
        "fee_currency": "BNB",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    Infura_parser_lookup.update_major_currency("BNB")
    result = prepare_parse_result(__file__)
    Infura_parser_lookup.update_major_currency("Ether")  # patch back
    assert len(result) == 1

    print(json.dumps(expected))
    print(json.dumps(result[0].to_dto().dict()))

    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
