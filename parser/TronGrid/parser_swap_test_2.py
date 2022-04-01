import json
from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = [{
        "trx_id": "e69eb9c45f315b6fb5d00f37c31a010d018d916117cc138b8ce3bd926e7fe4ee",
        "url": "https://tronscan.org/#/transaction/e69eb9c45f315b6fb5d00f37c31a010d018d916117cc138b8ce3bd926e7fe4ee",
        "type": "Swap",
        "status": "SUCCESS",
        "timestamp": "2020-09-12T07:33:27+00:00",
        "in_amount": "30307.606441",
        "in_amount_major": "30307.606441",
        "in_currency": "TRON",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": "1000.0",
        "out_amount_major": None,
        "out_currency": "USDT",
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.4057",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }]

    result = prepare_parse_result(__file__)

    assert len(result) == 1
    TestCase().assertDictEqual(expected[0], result[0].to_dto().dict())
