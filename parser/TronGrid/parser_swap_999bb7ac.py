from datetime import datetime

import pytz
from loguru import logger

from dto.TronGrid.contractType import ContractType
from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from parser.TronGrid.currencyLookup import contract_address_to_currency, \
    name_to_currency
from parser.base import BaseParser


class Parser(BaseParser):
    """
    default parser for swap transactions (trx purchase)
    example: https://tronscan.org/#/transaction/807e5694ea2397c8f874830c22ab30c41fe23e74f6f8dc59c68b1866486241f9
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
            has_valid_sigs = "transfer" in trx.events.get_event_by_index(0).event_name.lower().lower() and \
                             "approval" in trx.events.get_event_by_index(1).event_name.lower() and \
                             "trxpurchase" in trx.events.get_event_by_index(2).event_name.lower() and \
                             "snapshot" in trx.events.get_event_by_index(3).event_name.lower()

            return is_smart_contract and has_valid_sigs

        except Exception as e:
            logger.warning(f"failed to parse contract: {e}")
            return False

    def parse(self, trx: TrxDto) -> ParsedTrx:
        in_contract_addr = trx.events.get_event_by_index(0).contract_address

        event = trx.events.get_event_by_index(2)

        in_currency = name_to_currency("TRXToken")
        if not in_currency:
            raise ValueError(f"cannot find in currency: {in_contract_addr}")
        in_amount = event.result.get("trx_bought")
        if in_amount is None:
            raise ValueError("cannot find in amount")

        out_currency = contract_address_to_currency(in_contract_addr)
        out_amount = event.result.get("tokens_sold")
        if out_amount is None:
            raise ValueError("cannot find out amount")

        fee_currency = name_to_currency("TRXToken")
        fee_amount = str(trx.info.fee)

        return ParsedTrx(
            trx_id=trx.trx_id,
            url=f"https://tronscan.org/#/transaction/{trx.trx_id}",
            type=ParsedTrxType.Swap,
            status=trx.status,
            timestamp=datetime.fromtimestamp(trx.info.blockTimeStamp / 1000,
                                             tz=pytz.UTC),
            in_payload=TrxPayload(value=in_amount,
                                  currency=in_currency
                                  ),
            out_payload=TrxPayload(value=out_amount,
                                   currency=out_currency),
            fee_payload=TrxPayload(value=fee_amount,
                                   currency=fee_currency))
