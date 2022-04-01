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
    default parser for leave with dividend
    example: https://tronscan.org/#/transaction/6434790859e178c3981dede5b40d363f3b593701181a190c3477dfd3b20bcc5f
    """

    def can_handle(self, trx: TrxDto) -> bool:
        if trx.details.method_id == "d66d9e19":
            transfer_event_size = len(self.find_all_transfer_in_logs(trx))
            if transfer_event_size == 2:
                return True
            raise ValueError(
                f"leave with dividend (invalid number of transfer in logs); expected 2, actual {transfer_event_size}")
        return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = self.find_in_trx_log(trx)

        if not in_trx_log:
            raise ValueError("cannot find dividend event")

        fee_currency = self.major_currency
        fee_amount = str(trx.info.fee)

        return [ParsedTrx(
            trx_id=trx.trx_id,
            url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
            type=ParsedTrxType.Dividend,
            status=trx.status,
            timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000,
                                             tz=pytz.UTC),
            major_currency=self.major_currency,
            in_payload=TrxPayload(value=in_trx_log.result.get("value"),
                                  currency=TronGrid_currency_lookup.contract_address_to_currency(
                                      in_trx_log.contract_address)
                                  ),
            fee_payload=TrxPayload(value=fee_amount,
                                   currency=fee_currency))]

    def find_in_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_second_transfer_in_log(trx)
