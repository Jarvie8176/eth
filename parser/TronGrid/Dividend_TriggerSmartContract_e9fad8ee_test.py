from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "c5906208fa72274161a09b2a7a5444e6b50a8681359750f001d659616bccd0dd",
        "url": "https://tronscan.org/#/transaction/c5906208fa72274161a09b2a7a5444e6b50a8681359750f001d659616bccd0dd",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-11T22:02:09+00:00",
        "in_amount": "0.00201081314571313",
        "in_currency": "Tig",
        "fee_amount": "1.24132",
        "fee_currency": "TRON",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    TestCase().assertDictEqual(expected, prepare_parse_result(__file__).dict())
