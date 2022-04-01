from datetime import datetime
from typing import List, Optional

import pytz
from loguru import logger

from dto.TronGrid.event import EventDataDto
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, ParsedTrxType, TrxPayload
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.TronGrid.parser_base import TronGridParser


class Parser(TronGridParser):
    """
    default parser for swap
    example:
        https://tronscan.org/#/transaction/d6a9f0cb2bd9265a0af98737fef6b06d649c466c8a6c6de31211fa7b45290d04
        https://tronscan.org/#/transaction/e69eb9c45f315b6fb5d00f37c31a010d018d916117cc138b8ce3bd926e7fe4ee
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id in ["99a13409", "999bb7ac"]

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        swap_log = self.find_swap_log(trx)
        in_trx_log = self.find_in_trx_log(trx)
        out_trx_log = self.find_out_trx_log(trx)
        if not swap_log:
            raise ValueError("cannot find swap event")
        if not out_trx_log:
            raise ValueError("cannot find transfer out event")

        if not in_trx_log:
            logger.warning("no transfer in event, assuming transfer in as TRON")
            in_payload = TrxPayload(value=swap_log.result.get("trx_bought"),
                                    value_major=swap_log.result.get("trx_bought"),
                                    currency=self.major_currency)
        else:
            in_payload = TrxPayload(value=in_trx_log.result.get("value"),
                                    currency=TronGrid_currency_lookup.contract_address_to_currency(
                                        in_trx_log.contract_address))

        out_payload = TrxPayload(value=swap_log.result.get("tokens_sold"),
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

    def find_swap_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_first_event_by_name(trx, "TrxPurchase")

    def find_in_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_first_transfer_in_log(trx)

    def find_out_trx_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        return self.find_first_transfer_out_log(trx)
