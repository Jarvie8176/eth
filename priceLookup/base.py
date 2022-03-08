from abc import ABC, abstractmethod
import bisect
from datetime import datetime
from typing import List

from dto.price import PriceDto


class BasePriceLookup(ABC):
    @property
    @abstractmethod
    def unit(self) -> str:
        pass

    @abstractmethod
    def load(self) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.price_data: List[PriceDto] = []

    def time_to_price(self, timestamp: datetime) -> PriceDto:
        """
        Find the closest price at a given time
        """
        candidate = PriceDto(timestamp=timestamp, symbol="", close="")
        left_idx = bisect.bisect_left(self.price_data, candidate)
        left_idx = left_idx - 1  # shift to the actual left, not insert place
        right_idx = max(min(len(self.price_data) - 1, left_idx + 1), 0)

        left = self.price_data[left_idx]
        right = self.price_data[right_idx]

        closest = left if abs(timestamp - left.timestamp) < abs(
            timestamp - right.timestamp) else right

        return closest
