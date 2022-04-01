import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "4589993ef622127f7e58e05eb6d496ef2fd328ebcee40cb5ebf04639e8ca94dc",
        "url": "https://tronscan.org/#/transaction/4589993ef622127f7e58e05eb6d496ef2fd328ebcee40cb5ebf04639e8ca94dc",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-11T08:53:00+00:00",
        "in_amount": "0.433147696096882537",
        "in_amount_major": None,
        "in_currency": "KIT",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.95439",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    print(json.dumps(expected[0]))
    print(json.dumps(result[0].to_dto().dict()))


    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
