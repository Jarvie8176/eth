from abc import ABC, abstractmethod

from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx


class BaseParser(ABC):
    @abstractmethod
    def can_handle(self, trx: TrxDto) -> bool:
        return False

    @abstractmethod
    def parse(self, trx: TrxDto) -> ParsedTrx:
        raise NotImplementedError("not implemented")
