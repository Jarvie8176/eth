from typing import List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "removeLiquidityETHWithPermit", method_id: "0xded9382a"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0xded9382a" and self.assert_log_length(trx, 9)

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log_1 = trx.receipt.get_log_by_index(7)
        in_trx_log_2 = trx.receipt.get_log_by_index(4)

        if not in_trx_log_1:
            raise ValueError("cannot find transaction log of in event #1")
        if not in_trx_log_2:
            raise ValueError("cannot find transaction log of in event #2")

        in_payload_1 = TrxPayload(value=str(int(in_trx_log_1.data, 0)),
                                  value_major=None,
                                  currency=Infura_currency_lookup.contract_address_to_currency(in_trx_log_1.address))
        in_payload_2 = TrxPayload(value=str(int(in_trx_log_2.data, 0)),
                                  value_major=None,
                                  currency=self.major_currency)
        fee_payload = TrxPayload(value=trx.receipt.trx_fee,
                                 value_major=trx.receipt.trx_fee,
                                 currency=self.major_currency)

        parsed_trx_1 = ParsedTrx(trx_id=trx.trx_id,
                                 url=trx.url,
                                 type=ParsedTrxType.Buy,
                                 status=parse_status(trx.receipt.status),
                                 timestamp=trx.timestamp,
                                 major_currency=self.major_currency,
                                 in_payload=in_payload_1,
                                 out_payload=None,
                                 fee_payload=fee_payload)
        parsed_trx_2 = ParsedTrx(trx_id=trx.trx_id,
                                 url=trx.url,
                                 type=ParsedTrxType.Buy,
                                 status=parse_status(trx.receipt.status),
                                 timestamp=trx.timestamp,
                                 major_currency=self.major_currency,
                                 in_payload=in_payload_2,
                                 out_payload=None,
                                 fee_payload=None)
        return [parsed_trx_1, parsed_trx_2]
