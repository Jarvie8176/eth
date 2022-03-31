from dataclasses import dataclass
from typing import Optional

from pydantic.main import BaseModel


class FailedTrxDto(BaseModel):
    trx_id: Optional[str]
    url: Optional[str]
    method_id: Optional[str]
    err_details: str

@dataclass
class FailedTrx:
    trx_id: Optional[str]
    url: Optional[str]
    method_id: Optional[str]
    err: Exception

    def err_details(self) -> str:
        return f"{type(self.err).__name__}: {str(self.err)}"

    def to_dto(self) -> FailedTrxDto:
        return FailedTrxDto(trx_id=self.trx_id,
                            url=self.url,
                            method_id=self.method_id,
                            err_details=self.err_details())
