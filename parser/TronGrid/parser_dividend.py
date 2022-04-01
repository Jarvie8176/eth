from datetime import datetime
from typing import List

import pytz
from loguru import logger

from dto.TronGrid.transaction import TrxDto
from dto.TronGrid.contractType import ContractType
from dto.parsedTrx import ParsedTrx, ParsedTrxType, TrxPayload
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.TronGrid.parser_base import TronGridParser


class Parser(TronGridParser):
    """
    default parser for dividend transactions
    example: https://tronscan.org/#/transaction/235c1cf9df062dc49bd0a89b45332c93c81d4fceced7ea0a8883c4da999bf6c9
    """

    def can_handle(self, trx: TrxDto) -> bool:
        try:
            contract = trx.get_contract()
            if not contract:
                return False

            if trx.events.meta.page_size != 2:
                return False

            contract_type = contract.type

            events = [
                trx.events.get_event_by_index(0),
                trx.events.get_event_by_index(1)
            ]

            is_smart_contract = contract_type == ContractType.TriggerSmartContract
            has_valid_sigs = "transfer" in events[0].event_name.lower() and \
                             ("reward" in events[1].event_name.lower() or "withdrawn" in events[
                                 1].event_name.lower() or "airdrop" in events[1].event_name.lower())

            return is_smart_contract and has_valid_sigs and self.assert_log_length(trx, 2)

        except Exception as e:
            logger.warning(f"failed to parse contract: {e}")
            return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        event = trx.events.get_event_by_index(0)
        reward_contract_addr = event.contract_address

        reward_currency = TronGrid_currency_lookup.contract_address_to_currency(reward_contract_addr)
        if not reward_currency:
            raise ValueError(f"cannot find reward currency: {reward_contract_addr}")

        reward_amount = event.result.get("value")
        if reward_amount is None:
            reward_amount = event.result.get("wad")
            if reward_amount is None:
                raise ValueError("cannot find reward amount")

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
            in_payload=TrxPayload(value=reward_amount,
                                  currency=reward_currency
                                  ),
            fee_payload=TrxPayload(value=fee_amount,
                                   currency=fee_currency))]
