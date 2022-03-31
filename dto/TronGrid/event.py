from typing import Dict, List

from pydantic.main import BaseModel


class EventDataDto(BaseModel):
    block_number: int
    block_timestamp: int  # unix ts in ms
    caller_contract_address: str
    contract_address: str
    event_index: int
    event_name: str
    event: str
    transaction_id: str
    result: Dict[str, str]
    result_type: Dict[str, str]


class EventMetaDto(BaseModel):
    at: int  # unix ts in ms
    page_size: int


class TrxEventDto(BaseModel):
    tx_id: str
    success: bool
    data: List[EventDataDto]
    meta: EventMetaDto

    def get_event_by_index(self, idx: int) -> EventDataDto:
        try:
            return next(i for i in self.data if i.event_index == idx)
        except StopIteration:
            raise Exception("index out of range")
