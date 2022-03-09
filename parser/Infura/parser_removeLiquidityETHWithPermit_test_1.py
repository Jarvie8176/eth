from typing import List
from unittest import TestCase

from parser.Infura.util import prepare_parse_result


def test() -> None:
    expected = [{
        "trx_id": "0xb33493db233a9e7502453f8f39accdbb3b416b71f3d065106fe28f7dcab1b3cd",
        "url": "https://etherscan.io/tx/0xb33493db233a9e7502453f8f39accdbb3b416b71f3d065106fe28f7dcab1b3cd",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2020-08-29T09:34:13+00:00",
        "in_amount": "848.231895064720881391",
        "in_amount_major": None,
        "in_currency": "SUSHI",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.01974251",
        "fee_currency": "ETH",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "0xb33493db233a9e7502453f8f39accdbb3b416b71f3d065106fe28f7dcab1b3cd",
        "url": "https://etherscan.io/tx/0xb33493db233a9e7502453f8f39accdbb3b416b71f3d065106fe28f7dcab1b3cd",
        "type": "Buy",
        "status": "SUCCESS",
        "timestamp": "2020-08-29T09:34:13+00:00",
        "in_amount": "3.251267789175652099",
        "in_amount_major": "3.251267789175652099",
        "in_currency": "ETH",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": None,
        "fee_currency": None,
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result: List[ParsedTrx] = prepare_parse_result(__file__)  # type: ignore
    assert len(result) == 2

    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
    TestCase().assertDictEqual(expected[1], result[1].to_dto().dict())
