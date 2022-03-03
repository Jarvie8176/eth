from abc import ABC, abstractmethod

from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx


class BaseParser(ABC):
    def can_handle(self, trx: TrxDto) -> bool:
        return False

    @abstractmethod
    def parse(self, trx: TrxDto) -> ParsedTrx:
        raise NotImplementedError("not implemented")

    @property
    def load_order(self) -> int:
        """
        defined the priority of which parser to use, if there are multiple matches
        (higher order takes priority)
        :return:
        """
        return 0
