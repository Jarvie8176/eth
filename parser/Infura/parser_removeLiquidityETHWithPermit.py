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
        return trx.details.method_id == "0xded9382a"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        token_in_trx_log = self.find_first_transfer_in_log(trx)
        major_currency_in_trx_log = self.find_first_withdrawal_from_major_currency(trx)

        if not token_in_trx_log:
            raise ValueError("cannot find transaction log of in event #1")
        if not major_currency_in_trx_log:
            raise ValueError("cannot find transaction log of in event #2")

        in_payload_1 = TrxPayload(value=str(int(token_in_trx_log.data, 0)),
                                  value_major=None,
                                  currency=Infura_currency_lookup.contract_address_to_currency(token_in_trx_log.address))
        in_payload_2 = TrxPayload(value=str(int(major_currency_in_trx_log.data, 0)),
                                  value_major=str(int(major_currency_in_trx_log.data, 0)),
                                  currency=self.major_currency)
        fee_payload = TrxPayload(value=trx.trx_fee,
                                 value_major=trx.trx_fee,
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
