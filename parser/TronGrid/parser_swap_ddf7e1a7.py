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
    default parser for swap (between tokens)
    example:
        https://tronscan.org/#/transaction/4493595fc618e7a692ee7150a65fbd09bf6d0d6f71194aa883df38a85d9ca82f
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id == "ddf7e1a7"

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        swap_buy_log = self.find_first_event_by_name(trx, "TokenPurchase")
        swap_sell_log = self.find_first_event_by_name(trx, "TrxPurchase")

        if not swap_buy_log:
            raise ValueError("cannot find swap buy event")
        if not swap_sell_log:
            raise ValueError("cannot find swap sell event")

        in_trx_log = self.find_in_trx_log(trx)
        out_trx_log = self.find_out_trx_log(trx)

        if not in_trx_log:
            raise ValueError("cannot find transfer in event")
        if not out_trx_log:
            raise ValueError("cannot find transfer out event")

        in_payload = TrxPayload(value=swap_buy_log.result.get("tokens_bought"),
                                value_major=swap_buy_log.result.get("trx_sold"),
                                currency=TronGrid_currency_lookup.contract_address_to_currency(
                                    in_trx_log.contract_address))
        out_payload = TrxPayload(value=swap_sell_log.result.get("tokens_sold"),
                                 value_major=swap_sell_log.result.get("trx_bought"),
                                 currency=TronGrid_currency_lookup.contract_address_to_currency(
                                     out_trx_log.contract_address))
        fee_payload = TrxPayload(value=str(trx.info.fee),
                                 currency=self.major_currency)

        return [ParsedTrx(
            trx_id=trx.trx_id,
            url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
            type=ParsedTrxType.Swap,
            status=trx.status,
            timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000, tz=pytz.UTC),
            major_currency=self.major_currency,
            in_payload=in_payload,
            out_payload=out_payload,
            fee_payload=fee_payload)]

    def find_in_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_first_transfer_in_log(trx)

    def find_out_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_first_transfer_out_log(trx)
