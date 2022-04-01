import json
from os import path

from dto.TronGrid.transaction import TrxDto


def test_get_account():
    test_file = path.splitext(__file__)[0] + ".payload.txt"
    with open(test_file, "r") as f:
        trx_data = json.load(f)
    trx = TrxDto(**trx_data)

    assert trx.get_account_hex() == "0x2e4648a0d3bdec62fa6d38868019b7444c864157"
    assert trx.get_account_base58() == "TEBtHHE5Ve2vneTpcKo4UevB2tw1M8D7GN"


def test_get_log_by_index() -> None:
    test_file = path.splitext(__file__)[0] + ".payload.txt"
    with open(test_file, 'r') as f:
        trx_data = json.load(f)
    trx = TrxDto(**trx_data)

    assert trx.events.get_event_by_index(0).event_index == 0
    assert trx.events.get_event_by_index(1).event_index == 1
    assert trx.events.get_event_by_index(2).event_index == 2
    assert trx.events.get_event_by_index(5) is None
    assert trx.events.get_event_by_index(-1) is None
