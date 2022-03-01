from datetime import datetime

from dto.TronGrid.transaction import TrxDto
from dto.TronGrid.contractType import ContractType
from dto.TronGrid.triggerSmartContract import TriggerSmartContractDto
from dto.parsedTrx import ParsedTrx
from parser.tronGrid.base import BaseParser
from parser.tronGrid.currencyLookup import contract_address_to_currency, trx_token


class Parser(BaseParser):
    def can_handle(self, trx: TrxDto) -> bool:
        try:
            contract = TriggerSmartContractDto(**trx.get_contract())  # type: ignore
            contract_type = contract.type
            method_id = contract.parameter.value.data[:8]

            return contract_type == ContractType.TriggerSmartContract \
                and method_id == "1c4b774b"

        except Exception as e:
            print(e)
            raise e

    def parse(self, trx: TrxDto) -> ParsedTrx:
        event = trx.events.get_event_by_index(0)
        reward_contract_addr = event.contract_address

        reward_currency = contract_address_to_currency(reward_contract_addr)
        if not reward_currency:
            raise ValueError(f"cannot find reward currency: {reward_contract_addr}")

        reward_amount = event.result.get("value")
        if not reward_amount:
            raise ValueError("cannot find reward amount")

        fee_currency = trx_token
        fee_amount = str(trx.info.fee)

        timestamp = datetime.utcfromtimestamp(trx.info.blockTimeStamp / 1000)\
            .isoformat() + "Z"

        payload = {
            "trx_id": trx.trx_id,
            "url": f"https://tronscan.org/#/transaction/{trx.trx_id}",
            "type": "Dividend",
            "status": trx.status,
            "in_amount": reward_currency.to_readable_value(reward_amount),
            "timestamp": timestamp,
            "in_currency": reward_currency.unit,
            "fee_amount": fee_currency.to_readable_value(fee_amount),
            "fee_currency": fee_currency.unit
        }

        return ParsedTrx(**payload)
