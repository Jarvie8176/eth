from datetime import datetime
from typing import Any, List, Optional

import pytz
from pydantic import Field
from pydantic.main import BaseModel


class TrxDetailsDto(BaseModel):
    input: str
    gasPrice: str  # hex number

    @property
    def method_id(self) -> str:
        return self.input[:10]


class TrxLogDto(BaseModel):
    address: str
    blockHash: str
    blockNumber: str  # hex number
    data: str
    logIndex: str  # hex number
    removed: bool
    topics: List[str]
    transactionHash: str
    transactionIndex: str  # hex number


class TrxReceiptDto(BaseModel):
    class Config:
        allow_population_by_field_name = True

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        self.logs.sort(key=lambda log: int(log.logIndex, 0))

    blockHash: str
    blockNumber: str
    contractAddress: Optional[str]
    effectiveGasPrice: Optional[str]  # hex number
    from_: str = Field(alias="from")  # original attribute is from
    gasUsed: str  # hex number
    logsBloom: str
    status: str  # hex number
    to: str
    transactionHash: str
    transactionIndex: str  # hex number
    type: str  # hex number
    logs: List[TrxLogDto]

    def get_log_by_index(self, idx: int) -> Optional[TrxLogDto]:
        return self.logs[idx] if 0 <= idx < len(self.logs) else None


class TrxBlockDto(BaseModel):
    timestamp: str  # hex number


class TrxDto(BaseModel):
    details: TrxDetailsDto
    receipt: TrxReceiptDto
    block: TrxBlockDto

    @property
    def trx_id(self) -> str:
        return self.receipt.transactionHash

    @property
    def url(self) -> str:
        return f"https://etherscan.io/tx/{self.receipt.transactionHash}"

    @property
    def timestamp(self) -> datetime:
        return datetime.fromtimestamp(int(self.block.timestamp, 0), tz=pytz.UTC)

    @property
    def trx_fee(self) -> str:
        """
        :return: computed transaction fee
        """
        return str(int(self.details.gasPrice, 0) * int(self.receipt.gasUsed, 0))
