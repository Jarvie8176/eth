import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:

    expected = [{
        "trx_id": "bcf3eecd204aed9bd4312e2e41edc2428209ef0aaca881fcccd4c486bb33fb0f",
        "url": "https://tronscan.org/#/transaction/bcf3eecd204aed9bd4312e2e41edc2428209ef0aaca881fcccd4c486bb33fb0f",
        "type": "Sell",
        "status": "SUCCESS",
        "timestamp": "2020-09-13T08:48:33+00:00",
        "in_amount": None,
        "in_amount_major": None,
        "in_currency": None,
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "34.457223",
        "out_amount_major": "34.457223",
        "out_currency": "TRON",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.59288",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }, {
        "trx_id": "bcf3eecd204aed9bd4312e2e41edc2428209ef0aaca881fcccd4c486bb33fb0f",
        "url": "https://tronscan.org/#/transaction/bcf3eecd204aed9bd4312e2e41edc2428209ef0aaca881fcccd4c486bb33fb0f",
        "type": "Sell",
        "status": "SUCCESS",
        "timestamp": "2020-09-13T08:48:33+00:00",
        "in_amount": None,
        "in_amount_major": None,
        "in_currency": None,
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "0.999999991790055141",
        "out_amount_major": None,
        "out_currency": "USDJ",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": None,
        "fee_currency": None,
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]
    result = prepare_parse_result(__file__)

    assert len(result) == 2
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
    TestCase().assertDictEqual(expected[1], result[1].to_dto().dict())
