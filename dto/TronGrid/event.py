from typing import Dict, List, Any

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

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        self.data.sort(key=lambda log: log.event_index)

    def get_event_by_index(self, idx: int) -> EventDataDto:
        return self.data[idx] if 0 <= idx < len(self.data) else None
