from abc import ABC
from typing import Optional, Any

from dto.Infura.transaction import TrxDto, TrxLogDto
from models.exceptions import TrxLogLengthNotMatch
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.base import BaseParser
from parser.currency import Currency


class InfuraParser(BaseParser[TrxDto], ABC):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.major_currency_symbol = "Ether"

    @property
    def major_currency(self) -> Currency:
        return Infura_currency_lookup.name_to_currency(self.major_currency_symbol)

    def assert_log_length(self, trx: TrxDto, length: int) -> bool:
        # todo: add to tron parser
        log_len = len(trx.receipt.logs)
        if length != log_len:
            raise TrxLogLengthNotMatch(f"expected log length: {length}; actual: {log_len}")
        return True

    @staticmethod
    def find_first_transfer_in_log(trx: TrxDto) -> Optional[TrxLogDto]:
        """
        returns the first transfer event that transfers into [from address]
        :param trx:
        :return:
        """
        topic = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
        receiver_addr = trx.receipt.from_
        for log in trx.receipt.logs:
            is_transfer = int(log.topics[0], 0) == int(topic, 0)
            if not is_transfer:
                continue
            is_sent_to_receiver = int(log.topics[2], 0) == int(receiver_addr, 0)
            if is_sent_to_receiver:
                return log
        return None

    @staticmethod
    def find_first_transfer_out_log(trx: TrxDto) -> Optional[TrxLogDto]:
        """
        returns the first transfer event that transfers out of [from address]
        :param trx:
        :return:
        """
        topic = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
        receiver_addr = trx.receipt.from_
        for log in trx.receipt.logs:
            is_transfer = int(log.topics[0], 0) == int(topic, 0)
            if not is_transfer:
                continue
            is_sent_to_receiver = int(log.topics[1], 0) == int(receiver_addr, 0)
            if is_sent_to_receiver:
                return log
        return None

    def find_first_transafer_from_major_currency(self, trx: TrxDto) -> Optional[TrxLogDto]:
        """
        returns the first transfer event that is made from the major currency address
        :param trx:
        :return:
        """
        topic = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
        contract_addr = self.major_currency.contract_address
        for log in trx.receipt.logs:
            is_transfer = int(log.topics[0], 0) == int(topic, 0)
            if not is_transfer:
                continue
            is_from_major_currency_addr = int(log.address, 0) == int(contract_addr, 0)
            if is_from_major_currency_addr:
                return log
        return None

    def find_first_withdrawal_from_major_currency(self, trx: TrxDto) -> Optional[TrxLogDto]:
        """
        returns the first withdrawal event that is made from the major currency address
        :param trx:
        :return:
        """
        topic = "0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65"
        contract_addr = self.major_currency.contract_address
        for log in trx.receipt.logs:
            is_withdrawal = int(log.topics[0], 0) == int(topic, 0)
            if not is_withdrawal:
                continue
            is_from_major_currency_addr = int(log.address, 0) == int(contract_addr, 0)
            if is_from_major_currency_addr:
                return log
        return None
