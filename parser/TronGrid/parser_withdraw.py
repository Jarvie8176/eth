from datetime import datetime
from typing import List, Optional

import pytz

from dto.TronGrid.event import EventDataDto
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, ParsedTrxType, TrxPayload
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.TronGrid.parser_base import TronGridParser


class Parser(TronGridParser):
    """
    default parser for withdraw with dividend
    example: https://tronscan.org/#/transaction/4589993ef622127f7e58e05eb6d496ef2fd328ebcee40cb5ebf04639e8ca94dc/event-logs
    """

    def can_handle(self, trx: TrxDto) -> bool:
        if trx.details.method_id == "2e1a7d4d":
            transfer_in_log_size = len(self.find_all_transfer_in_logs(trx))
            if transfer_in_log_size != 2:
                raise ValueError(
                    f"withdraw with dividend: invalid transfer in log size: expected 2, actual {transfer_in_log_size}")
            return True
        return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = self.find_in_trx_log(trx)
        if not in_trx_log:
            raise ValueError("cannot find dividend event")

        in_payload = TrxPayload(value=in_trx_log.result.get("value"),
                                currency=TronGrid_currency_lookup.contract_address_to_currency(
                                    in_trx_log.contract_address))
        fee_payload = TrxPayload(value=str(trx.info.fee),
                                 currency=self.major_currency)

        return [ParsedTrx(
            trx_id=trx.trx_id,
            url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
            type=ParsedTrxType.Dividend,
            status=trx.status,
            timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000, tz=pytz.UTC),
            major_currency=self.major_currency,
            in_payload=in_payload,
            fee_payload=fee_payload)]

    def find_in_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_first_transfer_in_log(trx)
