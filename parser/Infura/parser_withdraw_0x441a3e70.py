from typing import List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "withdraw", method_id: "0x441a3e70" (withdraw from token with dividend)
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0x441a3e70"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = trx.receipt.get_log_by_index(2)

        if not in_trx_log:
            raise ValueError("cannot find transaction log of in event")

        in_payload = TrxPayload(value=str(int(in_trx_log.data, 0)),
                                currency=Infura_currency_lookup.contract_address_to_currency(in_trx_log.address))
        out_payload = None
        fee_payload = TrxPayload(value=trx.receipt.trx_fee,
                                 value_major=trx.receipt.trx_fee,
                                 currency=self.major_currency)

        return [ParsedTrx(trx_id=trx.trx_id,
                          url=trx.url,
                          type=ParsedTrxType.Dividend,
                          status=parse_status(trx.receipt.status),
                          timestamp=trx.timestamp,
                          major_currency=self.major_currency,
                          in_payload=in_payload,
                          out_payload=out_payload,
                          fee_payload=fee_payload)]
