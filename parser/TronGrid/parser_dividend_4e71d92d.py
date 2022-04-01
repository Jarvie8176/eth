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
    parser for a specific transaction
    example: https://tronscan.org/#/transaction/199a0d03921597ab1561512943f9d80a0635a37a6ba15759b8d6ec32ea50e4ca
    """

    def can_handle(self, trx: TrxDto) -> bool:
        if trx.details.method_id in ["4e71d92d", "3d18b912"]:
            transfer_event_size = len(self.find_all_transfer_in_logs(trx))
            if transfer_event_size == 1:
                return True
            raise ValueError(
                f"claim with dividend (invalid number of transfer in logs); expected 1, actual {transfer_event_size}")
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
        return self.find_first_transfer_in_log(trx)
