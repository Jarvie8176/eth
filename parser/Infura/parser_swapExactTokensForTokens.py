from typing import List, Optional

from dto.Infura.transaction import TrxDto, TrxLogDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "swapExactTokensForTokens", method_id: "0x38ed1739"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0x38ed1739"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = self.find_in_trx_log(trx)
        out_trx_log = self.find_out_trx_log(trx)
        value_equiv_log = self.find_value_equiv_trx_log(trx)

        if not in_trx_log:
            raise ValueError("cannot find transaction log of in event")
        if not out_trx_log:
            raise ValueError("cannot find transaction log of out event")

        value_major = None if not value_equiv_log else str(int(value_equiv_log.data, 0))

        in_payload = TrxPayload(value=str(int(in_trx_log.data, 0)),
                                value_major=value_major,
                                currency=Infura_currency_lookup.contract_address_to_currency(in_trx_log.address))
        out_payload = TrxPayload(value=str(int(out_trx_log.data, 0)),
                                 value_major=value_major,
                                 currency=Infura_currency_lookup.contract_address_to_currency(out_trx_log.address))
        fee_payload = TrxPayload(value=trx.trx_fee,
                                 value_major=trx.trx_fee,
                                 currency=self.major_currency)

        return [ParsedTrx(trx_id=trx.trx_id,
                          url=trx.url,
                          type=ParsedTrxType.Swap,
                          status=parse_status(trx.receipt.status),
                          timestamp=trx.timestamp,
                          major_currency=self.major_currency,
                          in_payload=in_payload,
                          out_payload=out_payload,
                          fee_payload=fee_payload)]

    def find_in_trx_log(self, trx: TrxDto) -> Optional[TrxLogDto]:
        return self.find_first_transfer_in_log(trx)

    def find_out_trx_log(self, trx: TrxDto) -> Optional[TrxLogDto]:
        return self.find_first_transfer_out_log(trx)

    def find_value_equiv_trx_log(self, trx: TrxDto) -> Optional[TrxLogDto]:
        return self.find_first_transfer_from_major_currency(trx)
