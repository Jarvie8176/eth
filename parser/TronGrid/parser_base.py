from abc import ABC
from typing import Any, Optional, List

from dto.TronGrid.event import EventDataDto
from dto.TronGrid.transaction import TrxDto
from models.exceptions import TrxLogLengthNotMatch
from parser.TronGrid.defn_currency import TronGrid_currency_lookup
from parser.base import BaseParser
from parser.currency import Currency


class TronGridParser(BaseParser[TrxDto], ABC):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.major_currency_symbol = "TRXToken"

    @property
    def major_currency(self) -> Currency:
        return TronGrid_currency_lookup.name_to_currency(self.major_currency_symbol)

    def assert_log_length(self, trx: TrxDto, length: int) -> bool:
        log_len = len(trx.events.data)
        if length != log_len:
            raise TrxLogLengthNotMatch(f"expected log length: {length}; actual: {log_len}")
        return True

    def find_first_transfer_in_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        """
        returns the first transfer events that transfers into [account address]
        :param trx:
        :return:
        """
        event_name = "Transfer"
        account_addr = trx.get_account_hex()
        for log in trx.events.data:
            is_transfer = log.event_name == event_name
            if not is_transfer:
                continue
            is_sent_to_receiver = log.result.get("to") == account_addr or log.result.get(
                "_to") == account_addr or log.result.get("dst") == account_addr
            if is_sent_to_receiver:
                return log
        return None

    def find_second_transfer_in_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        """
        returns the second transfer events that transfers into [account address]
        :param trx:
        :return:
        """
        event_name = "Transfer"
        account_addr = trx.get_account_hex()
        first_found = False
        for log in trx.events.data:
            is_transfer = log.event_name == event_name
            if not is_transfer:
                continue
            is_sent_to_receiver = log.result.get("to") == account_addr or log.result.get(
                "_to") == account_addr or log.result.get("dst") == account_addr
            if is_sent_to_receiver:
                if first_found:
                    return log
                else:
                    first_found = True
                    continue
        return None

    def find_all_transfer_in_logs(self, trx: TrxDto) -> List[EventDataDto]:
        """
        returns all transfer events that transfers into [account address]
        :param trx:
        :return:
        """
        event_name = "Transfer"
        account_addr = trx.get_account_hex()
        result = []
        for log in trx.events.data:
            is_transfer = log.event_name == event_name
            if not is_transfer:
                continue
            is_sent_to_receiver = log.result.get("to") == account_addr or log.result.get(
                "_to") == account_addr or log.result.get("dst") == account_addr
            if is_sent_to_receiver:
                result.append(log)
        return result

    def find_first_transfer_out_log(self, trx: TrxDto) -> Optional[EventDataDto]:
        """
        returns the first transfer events that transfers from [account address]
        :param trx:
        :return:
        """
        event_name = "Transfer"
        account_addr = trx.get_account_hex()
        for log in trx.events.data:
            is_transfer = log.event_name == event_name
            if not is_transfer:
                continue
            is_sent_to_receiver = log.result.get("from") == account_addr or log.result.get("_from") == account_addr or log.result.get("src") == account_addr
            if is_sent_to_receiver:
                return log
        return None

    def find_all_transfer_out_logs(self, trx: TrxDto) -> List[EventDataDto]:
        """
        returns all transfer events that transfers from [account address]
        :param trx:
        :return:
        """
        event_name = "Transfer"
        account_addr = trx.get_account_hex()
        result = []
        for log in trx.events.data:
            is_transfer = log.event_name == event_name
            if not is_transfer:
                continue
            is_sent_to_receiver = log.result.get("from") == account_addr or log.result.get("_from") == account_addr or log.result.get("src") == account_addr
            if is_sent_to_receiver:
                result.append(log)
        return result

    def find_add_liquidity_event(self, trx: TrxDto) -> Optional[EventDataDto]:
        """
        returns the first AddLiquidity event
        :param trx:
        :return:
        """
        event_name = "AddLiquidity"
        account_addr = trx.get_account_hex()
        for log in trx.events.data:
            is_matching_event = log.event_name == event_name
            if not is_matching_event:
                continue
            is_from_account = log.result.get("provider") == account_addr
            if is_from_account:
                return log
        return None

    def find_remove_liquidity_event(self, trx: TrxDto) -> Optional[EventDataDto]:
        """
        returns the first RemoveLiquidity event
        :param trx:
        :return:
        """
        event_name = "RemoveLiquidity"
        account_addr = trx.get_account_hex()
        for log in trx.events.data:
            is_matching_event = log.event_name == event_name
            if not is_matching_event:
                continue
            is_from_account = log.result.get("provider") == account_addr
            if is_from_account:
                return log
        return None

    def find_first_event_by_name(self, trx: TrxDto, event_name: str) -> Optional[EventDataDto]:
        """
        :param trx:
        :param event_name:
        :return: the first event that matches event name
        """
        for log in trx.events.data:
            is_matching_event = log.event_name == event_name
            if is_matching_event:
                return log
        return None
