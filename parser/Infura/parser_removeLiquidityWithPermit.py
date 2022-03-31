from typing import List, Optional

from dto.Infura.transaction import TrxDto, TrxLogDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "removeLiquidityWithPermit", method_id: "0x2195995c"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "0x2195995c"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log_1 = self.find_in_trx_log_1(trx)
        in_trx_log_2 = self.find_in_trx_log_2(trx)

        if not in_trx_log_1:
            raise ValueError("cannot find transaction log of in event #1")
        if not in_trx_log_2:
            raise ValueError("cannot find transaction log of in event #2")

        fee_payload = TrxPayload(value=trx.trx_fee,
                                 value_major=trx.trx_fee,
                                 currency=self.major_currency)
        in_payload_1 = TrxPayload(value=str(int(in_trx_log_1.data, 0)),
                                  value_major=None,
                                  currency=Infura_currency_lookup.contract_address_to_currency(in_trx_log_1.address))
        in_payload_2 = TrxPayload(value=str(int(in_trx_log_2.data, 0)),
                                  value_major=None,
                                  currency=Infura_currency_lookup.contract_address_to_currency(in_trx_log_2.address))

        return [ParsedTrx(trx_id=trx.trx_id,
                          url=trx.url,
                          type=ParsedTrxType.Buy,
                          status=parse_status(trx.receipt.status),
                          timestamp=trx.timestamp,
                          major_currency=self.major_currency,
                          in_payload=in_payload_1,
                          out_payload=None,
                          fee_payload=fee_payload),
                ParsedTrx(trx_id=trx.trx_id,
                          url=trx.url,
                          type=ParsedTrxType.Buy,
                          status=parse_status(trx.receipt.status),
                          timestamp=trx.timestamp,
                          major_currency=self.major_currency,
                          in_payload=in_payload_2,
                          out_payload=None,
                          fee_payload=None)]

    def find_in_trx_log_1(self, trx: TrxDto) -> Optional[TrxLogDto]:
        return self.find_first_transfer_in_log(trx)

    def find_in_trx_log_2(self, trx: TrxDto) -> Optional[TrxLogDto]:
        return self.find_second_transfer_in_log(trx)

    def find_out_trx_log(self, trx: TrxDto) -> Optional[TrxLogDto]:
        return self.find_first_transfer_out_log(trx)
