from unittest import TestCase
from parser.TronGrid.util import prepare_parse_result


def test_usage() -> None:
    expected = {
        "trx_id": "07510e7f31872664a7ab809adb5a483af96feba9fc03750ee3f3aafba69a7a88",
        "url": "https://tronscan.org/#/transaction/07510e7f31872664a7ab809adb5a483af96feba9fc03750ee3f3aafba69a7a88",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-14T03:17:15+00:00",
        "in_amount": "16.108070879600273167",
        "in_amount_major": None,
        "in_currency": "Tig",
        "in_rate": None,
        "in_rate_unit": None,
        "in_rate_timestamp": None,
        "out_amount": None,
        "out_amount_major": None,
        "out_currency": None,
        "out_rate": None,
        "out_rate_unit": None,
        "out_rate_timestamp": None,
        "fee_amount": "0.82927",
        "fee_currency": "TRON",
        "fee_rate": None,
        "fee_rate_unit": None,
        "fee_rate_timestamp": None,
    }

    result = prepare_parse_result(__file__)
    assert len(result) == 1
    TestCase().assertDictEqual(expected, result[0].to_dto().dict())
