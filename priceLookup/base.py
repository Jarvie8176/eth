from abc import ABC, abstractmethod
from datetime import datetime

from dto.price import PriceDto


class BasePriceLookup(ABC):
    @property
    @abstractmethod
    def unit(self) -> str:
        pass

    @abstractmethod
    def load(self) -> None:
        pass

    """
    Find the closest price at a given time
    """
    @abstractmethod
    def time_to_price(self, timestamp: datetime) -> PriceDto:
        pass
