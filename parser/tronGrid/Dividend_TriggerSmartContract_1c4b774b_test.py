import json
import pathlib
from os import path
from unittest import TestCase

from dto.TronGrid.transaction import TrxDto
from parser.tronGrid import Dividend_TriggerSmartContract_1c4b774b


def test_usage() -> None:
    payload_file = path.join(pathlib.Path(__file__).parent.resolve(),
                             "Dividend_TriggerSmartContract_1c4b774b_test.payload.txt")
    with open(payload_file, "r") as f:
        trx_data = json.loads(f.read())

    trx = TrxDto(**trx_data)
    parser = Dividend_TriggerSmartContract_1c4b774b.Parser()
    result = parser.parse(trx).dict()

    expected = {
        "trx_id": "235c1cf9df062dc49bd0a89b45332c93c81d4fceced7ea0a8883c4da999bf6c9",
        "url": "https://tronscan.org/#/transaction/235c1cf9df062dc49bd0a89b45332c93c81d4fceced7ea0a8883c4da999bf6c9",
        "type": "Dividend",
        "status": "SUCCESS",
        "timestamp": "2020-09-27T02:58:51Z",
        "in_amount": "2363.782943",
        "in_currency": "GOLD",
        "fee_amount": "0.66087",
        "fee_currency": "TRON"
    }

    TestCase().assertDictEqual(expected, result)
