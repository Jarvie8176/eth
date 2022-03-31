from typing import List, Optional

from dto.Infura.transaction import TrxDto, TrxLogDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status

from loguru import logger


class Parser(InfuraParser):
    """
    default parser of "addLiquidity", method_id: "0x4d49e87d"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id in ["0x4d49e87d", "0x4515cef3", "0xe8e33700"]

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_logs = self.find_in_trx_logs(trx)

        if not len(in_trx_logs):
            logger.debug("cannot find any transfer out event")
            return []

        fee_payload = TrxPayload(value=trx.trx_fee,
                                 value_major=trx.trx_fee,
                                 currency=self.major_currency)

        result = [ParsedTrx(trx_id=trx.trx_id,
                            url=trx.url,
                            type=ParsedTrxType.Sell,
                            status=parse_status(trx.receipt.status),
                            timestamp=trx.timestamp,
                            major_currency=self.major_currency,
                            out_payload=TrxPayload(value=str(int(trx_log.data, 0)),
                                                   currency=Infura_currency_lookup.contract_address_to_currency(
                                                       trx_log.address)))
                  for trx_log in in_trx_logs]

        result[0].fee_payload = fee_payload
        return result

    def find_in_trx_logs(self, trx: TrxDto) -> List[TrxLogDto]:
        return self.find_all_transfer_out_logs(trx)
