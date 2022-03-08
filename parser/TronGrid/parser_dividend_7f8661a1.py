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
    parser for a specific transaction
    example: https://tronscan.org/#/transaction/035ac031e657c9370f2a7470f8673d23ee576176b57c3a92b6c870adaff2c0f1
    """

    def can_handle(self, trx: TrxDto) -> bool:
        try:
            contract = trx.get_contract()
            if not contract:
                return False

            if trx.events.meta.page_size != 4:
                return False

            contract_type = contract.type

            is_smart_contract = contract_type == ContractType.TriggerSmartContract
            has_valid_sigs = "transfer" in trx.events.get_event_by_index(0).event_name.lower() and \
                             "withdrawn" in trx.events.get_event_by_index(1).event_name.lower() and \
                             "transfer" in trx.events.get_event_by_index(2).event_name.lower() and \
                             "rewardpaid" in trx.events.get_event_by_index(3).event_name.lower()

            return is_smart_contract and has_valid_sigs

        except Exception as e:
            logger.warning(f"failed to parse contract: {e}")
            return False

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        event = trx.events.get_event_by_index(2)
        reward_contract_addr = event.contract_address

        reward_currency = TronGrid_currency_lookup.contract_address_to_currency(reward_contract_addr)
        if not reward_currency:
            raise ValueError(f"cannot find reward currency: {reward_contract_addr}")

        reward_amount = event.result.get("value")
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
