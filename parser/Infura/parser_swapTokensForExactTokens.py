from typing import List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "swapExactTokensForTokens", method_id: "0x8803dbee"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0x8803dbee" and self.assert_log_length(trx, 7)

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = trx.receipt.get_log_by_index(4)
        out_trx_log = trx.receipt.get_log_by_index(0)
        value_equiv_log = trx.receipt.get_log_by_index(1)

        if not in_trx_log:
            raise ValueError("cannot find transaction log of in event")
        if not out_trx_log:
            raise ValueError("cannot find transaction log of out event")
        if not value_equiv_log:
            raise ValueError("cannot find transaction log of value equiv event")

        in_payload = TrxPayload(value=str(int(in_trx_log.data, 0)),
                                value_major=str(int(value_equiv_log.data, 0)),
                                currency=Infura_currency_lookup.contract_address_to_currency(in_trx_log.address))
        out_payload = TrxPayload(value=str(int(out_trx_log.data, 0)),
                                 value_major=str(int(value_equiv_log.data, 0)),
                                 currency=Infura_currency_lookup.contract_address_to_currency(out_trx_log.address))
        fee_payload = TrxPayload(value=trx.receipt.trx_fee,
                                 value_major=trx.receipt.trx_fee,
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
