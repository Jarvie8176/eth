from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "807e5694ea2397c8f874830c22ab30c41fe23e74f6f8dc59c68b1866486241f9",
        "url": "https://tronscan.org/#/transaction/807e5694ea2397c8f874830c22ab30c41fe23e74f6f8dc59c68b1866486241f9",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-29T00:23:33+00:00",
        "in_amount": "51.771057",
        "in_amount_major": "51.771057",
        "in_currency": "TRON",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "0.094712852088814279",
        "out_amount_major": "51.771057",
        "out_currency": "SUNOLD",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.45685",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
