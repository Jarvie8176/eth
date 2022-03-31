import dateutil.parser
from typing import Dict, List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, ParsedTrxStatus, ParsedTrxType, TrxPayload
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.parser_base import InfuraParser

# SkippedMethod(method_id="0x1d572320", name="zapIn"),  # todo

transaction_ids: Dict[str, List[ParsedTrx]] = {
    # EtherScan
    "0xab9046b504b88cf9c1716388f93426cc3348497d92e2eb633c1c6ee584989bc6": [
        ParsedTrx(trx_id="0xab9046b504b88cf9c1716388f93426cc3348497d92e2eb633c1c6ee584989bc6",
                  url="https://etherscan.io/tx/0xab9046b504b88cf9c1716388f93426cc3348497d92e2eb633c1c6ee584989bc6",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2020-08-29T02:14:25Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("Ether"),
                  out_payload=TrxPayload(
                      value="60000000000000000000",
                      value_major="60000000000000000000",
                      currency=Infura_currency_lookup.name_to_currency("SushiToken")),
                  fee_payload=TrxPayload(
                      value="22515684000000000",
                      value_major="22515684000000000",
                      currency=Infura_currency_lookup.name_to_currency("Ether"),
                  )),
    ],
    "0x60112abc35c3582b3e1ff12619863efb85d328cb4b2a3f80c57b520c3edb101b": [
        ParsedTrx(trx_id="0x60112abc35c3582b3e1ff12619863efb85d328cb4b2a3f80c57b520c3edb101b",
                  url="https://etherscan.io/tx/0x60112abc35c3582b3e1ff12619863efb85d328cb4b2a3f80c57b520c3edb101b",
                  type=ParsedTrxType.Buy,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2020-09-01T16:54:06Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("Ether"),
                  in_payload=TrxPayload(
                      value="5920516206193865947",
                      value_major="5920516206193865947",
                      currency=Infura_currency_lookup.name_to_currency("Ether")),
                  fee_payload=TrxPayload(
                      value="56582694000000000",
                      value_major="56582694000000000",
                      currency=Infura_currency_lookup.name_to_currency("Ether"),
                  )),
        ParsedTrx(trx_id="0x60112abc35c3582b3e1ff12619863efb85d328cb4b2a3f80c57b520c3edb101b",
                  url="https://etherscan.io/tx/0x60112abc35c3582b3e1ff12619863efb85d328cb4b2a3f80c57b520c3edb101b",
                  type=ParsedTrxType.Dividend,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2020-09-01T16:54:06Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("YFValue"),
                  in_payload=TrxPayload(
                      value="854299883284305011",
                      value_major="854299883284305011",
                      currency=Infura_currency_lookup.name_to_currency("Ether"))),
    ],
    "0xd26d3ec73fa48a7abed22aa9ae069c0696ca2da62b7df25c3b88c0ae09083d3b": [
        ParsedTrx(trx_id="0xd26d3ec73fa48a7abed22aa9ae069c0696ca2da62b7df25c3b88c0ae09083d3b",
                  url="https://etherscan.io/tx/0xd26d3ec73fa48a7abed22aa9ae069c0696ca2da62b7df25c3b88c0ae09083d3b",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2020-08-31T20:52:09Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("Ether"),
                  out_payload=TrxPayload(
                      value="6000000000000000000",
                      value_major="6000000000000000000",
                      currency=Infura_currency_lookup.name_to_currency("Ether")),
                  fee_payload=TrxPayload(
                      value="22812479999873264",
                      value_major="22812479999873264",
                      currency=Infura_currency_lookup.name_to_currency("Ether"),
                  )),
    ],

    # BscScan
    "0xaecea797ee63ec05f29eca23e7359633b14c269b29f74ba9463e1dac087dc2eb": [
        ParsedTrx(trx_id="0xaecea797ee63ec05f29eca23e7359633b14c269b29f74ba9463e1dac087dc2eb",
                  url="https://bscscan.com/tx/0xaecea797ee63ec05f29eca23e7359633b14c269b29f74ba9463e1dac087dc2eb",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-03-24T03:27:47Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  out_payload=TrxPayload(
                      value="79611550000000000000000",
                      currency=Infura_currency_lookup.name_to_currency("Binance-Peg BUSD Token")),
                  fee_payload=TrxPayload(
                      value="1699533000000000",
                      value_major="1699533000000000",
                      currency=Infura_currency_lookup.name_to_currency("BNB"),
                  )),
        ParsedTrx(trx_id="0xaecea797ee63ec05f29eca23e7359633b14c269b29f74ba9463e1dac087dc2eb",
                  url="https://bscscan.com/tx/0xaecea797ee63ec05f29eca23e7359633b14c269b29f74ba9463e1dac087dc2eb",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-03-24T03:27:47Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  out_payload=TrxPayload(
                      value="1613375345382781038444",
                      currency=Infura_currency_lookup.name_to_currency("Binance-Peg USD Coin")))],
    "0x344d497fe6b92dfa0842e4ce2b19256b3101fdf086e6edd63cfe9bef6f8e1893": [
        ParsedTrx(trx_id="0x344d497fe6b92dfa0842e4ce2b19256b3101fdf086e6edd63cfe9bef6f8e1893",
                  url="https://bscscan.com/tx/0x344d497fe6b92dfa0842e4ce2b19256b3101fdf086e6edd63cfe9bef6f8e1893",
                  type=ParsedTrxType.Dividend,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-03-24T22:34:04Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=TrxPayload(
                      value="3685145699055508393",
                      currency=Infura_currency_lookup.name_to_currency("Ellipsis")),
                  fee_payload=TrxPayload(
                      value="3300528000000000",
                      value_major="3300528000000000",
                      currency=Infura_currency_lookup.name_to_currency("BNB")))
    ],
    "0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670": [
        # getReward(): swap; swap; add liquidity
        ParsedTrx(trx_id="0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  url="https://bscscan.com/tx/0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  type=ParsedTrxType.Swap,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-04-27T22:26:50Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=TrxPayload(
                      value="32507689407760639",
                      value_major="32507689407760639",
                      currency=Infura_currency_lookup.name_to_currency("BNB")),
                  out_payload=TrxPayload(
                      value="517528253154532242",
                      value_major="32507689407760639",
                      currency=Infura_currency_lookup.name_to_currency("PancakeSwap Token")),
                  fee_payload=TrxPayload(
                      value="4015425000000000",
                      value_major="4015425000000000",
                      currency=Infura_currency_lookup.name_to_currency("BNB"))),
        ParsedTrx(trx_id="0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  url="https://bscscan.com/tx/0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  type=ParsedTrxType.Swap,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-04-27T22:26:50Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=TrxPayload(
                      value="19202178128126574",
                      value_major="16253844703880319",
                      currency=Infura_currency_lookup.name_to_currency("Bunny Token")),
                  out_payload=TrxPayload(
                      value="16253844703880319",
                      value_major="16253844703880319",
                      currency=Infura_currency_lookup.name_to_currency("BNB")),
                  fee_payload=None),
        ParsedTrx(trx_id="0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  url="https://bscscan.com/tx/0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  type=ParsedTrxType.Swap,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-04-27T22:26:50Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=TrxPayload(
                      value="19202178128126574",
                      value_major="16253844703880319",
                      currency=Infura_currency_lookup.name_to_currency("Bunny Token")),
                  out_payload=TrxPayload(
                      value="16253844703880319",
                      value_major="16253844703880319",
                      currency=Infura_currency_lookup.name_to_currency("BNB")),
                  fee_payload=None),
        ParsedTrx(trx_id="0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  url="https://bscscan.com/tx/0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-04-27T22:26:50Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=None,
                  out_payload=TrxPayload(
                      value="16221340884050186",
                      value_major="16221340884050186",
                      currency=Infura_currency_lookup.name_to_currency("BNB")),
                  fee_payload=None),
        ParsedTrx(trx_id="0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  url="https://bscscan.com/tx/0x46fdfc2a5d024541b217f898426a8e73bb6e47f042f8d12e22262d93d1659670",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-04-27T22:26:50Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=None,
                  out_payload=TrxPayload(
                      value="19202178128126574",
                      currency=Infura_currency_lookup.name_to_currency("Bunny Token")),
                  fee_payload=None)
    ],
    "0x0e8f7f2035e7035ddf994e2c3471b8d094dd8432ac3d64c31f8b42c80446a798": [
        # zap in
        ParsedTrx(trx_id="0x0e8f7f2035e7035ddf994e2c3471b8d094dd8432ac3d64c31f8b42c80446a798",
                  url="https://bscscan.com/tx/0x0e8f7f2035e7035ddf994e2c3471b8d094dd8432ac3d64c31f8b42c80446a798",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-04-26T23:48:33Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=None,
                  out_payload=TrxPayload(
                      value="38394165413769546361006",
                      currency=Infura_currency_lookup.name_to_currency("Binance-Peg BUSD Token")),
                  fee_payload=TrxPayload(
                      value="1488665000000000",
                      value_major="1488665000000000",
                      currency=Infura_currency_lookup.name_to_currency("BNB"))),
        ParsedTrx(trx_id="0x0e8f7f2035e7035ddf994e2c3471b8d094dd8432ac3d64c31f8b42c80446a798",
                  url="https://bscscan.com/tx/0x0e8f7f2035e7035ddf994e2c3471b8d094dd8432ac3d64c31f8b42c80446a798",
                  type=ParsedTrxType.Sell,
                  status=ParsedTrxStatus.Success,
                  timestamp=dateutil.parser.parse("2021-04-26T23:48:33Z"),
                  major_currency=Infura_currency_lookup.name_to_currency("BNB"),
                  in_payload=None,
                  out_payload=TrxPayload(
                      value="72500000000000000000",
                      value_major="72500000000000000000",
                      currency=Infura_currency_lookup.name_to_currency("Wrapped BNB")),
                  fee_payload=None)
    ]
}


class Parser(InfuraParser):
    """
    parser for transactions with hard coded results
    """

    @property
    def load_order(self) -> int:
        return 9999

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.trx_id in transaction_ids.keys()

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        result = transaction_ids.get(trx.trx_id)
        if not result:
            raise ValueError("transaction is in hard coded list but no result")
        return result
