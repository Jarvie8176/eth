from abc import ABC, abstractmethod
from typing import Union, TypeVar, Generic, List
from pydantic.generics import GenericModel

from dto.Infura.transaction import TrxDto as InfuraTrxDto
from dto.TronGrid.transaction import TrxDto as TronTrxDto
from dto.parsedTrx import ParsedTrx

AnyTrxDto = Union[InfuraTrxDto, TronTrxDto]

TrxDtoType = TypeVar("TrxDtoType")


class BaseParser(ABC, GenericModel, Generic[TrxDtoType]):
    def can_handle(self, trx: TrxDtoType) -> bool:
        return False

    @abstractmethod
    def parse(self, trx: TrxDtoType) -> List[ParsedTrx]:
        raise NotImplementedError("not implemented")

    @property
    def load_order(self) -> int:
        """
        defined the priority of which parser to use, if there are multiple matches
        (higher order takes priority)
        :return:
        """
        return 0

    @abstractmethod
    def assert_log_length(self, trx: TrxDtoType, length: int) -> bool:
        pass
