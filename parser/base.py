from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Union

from dto.Infura.transaction import TrxDto as InfuraTrxDto
from dto.TronGrid.transaction import TrxDto as TronTrxDto
from dto.parsedTrx import ParsedTrx

AnyTrxDto = Union[InfuraTrxDto, TronTrxDto]

TrxDtoType = TypeVar("TrxDtoType")


class BaseParser(ABC, Generic[TrxDtoType]):
    def __init__(self) -> None:
        super().__init__()
        self.major_currency_symbol: str = ""

    @property
    def load_order(self) -> int:
        """
        defined the priority of which parser to use, if there are multiple matches
        (higher order takes priority)
        :return:
        """
        return 0

    def set_major_currency(self, symbol: str) -> None:
        self.major_currency_symbol = symbol

    @abstractmethod
    def can_handle(self, trx: TrxDtoType) -> bool:
        raise NotImplementedError("not implemented")

    @abstractmethod
    def parse(self, trx: TrxDtoType) -> List[ParsedTrx]:
        raise NotImplementedError("not implemented")

    @abstractmethod
    def assert_log_length(self, trx: TrxDtoType, length: int) -> bool:
        pass
