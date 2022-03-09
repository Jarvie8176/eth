from typing import List

from dto.Infura.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "addLiquidityETH", method_id: "0xf305d719"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0xf305d719" and self.assert_log_length(trx, 7)

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = trx.receipt.get_log_by_index(2)
        out_trx_log = trx.receipt.get_log_by_index(0)

        if not in_trx_log:
            raise ValueError("cannot find transaction log of in event")
        if not out_trx_log:
            raise ValueError("cannot find transaction log of out event")

        in_payload = TrxPayload(value=str(int(in_trx_log.data, 0)),
                                value_major=str(int(in_trx_log.data, 0)),
                                currency=self.major_currency)
        out_payload = TrxPayload(value=str(int(out_trx_log.data, 0)),
                                 value_major=str(int(in_trx_log.data, 0)),
                                 currency=Infura_currency_lookup.contract_address_to_currency(out_trx_log.address))
        fee_payload = TrxPayload(value=trx.receipt.trx_fee,
                                 value_major=trx.receipt.trx_fee,
                                 currency=self.major_currency)

        return [ParsedTrx(trx_id=trx.trx_id,
                          url=trx.url,
                          type=ParsedTrxType.Sell,
                          status=parse_status(trx.receipt.status),
                          timestamp=trx.timestamp,
                          major_currency=self.major_currency,
                          in_payload=in_payload,
                          out_payload=out_payload,
                          fee_payload=fee_payload)]
