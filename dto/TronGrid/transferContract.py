from typing import Literal

from pydantic import BaseModel

from dto.TronGrid.contractType import ContractType


class ParameterValueDto(BaseModel):
    amount: int
    owner_address: str
    to_address: str


class ParameterDto(BaseModel):
    value: ParameterValueDto
    type_url: str


class TransferContractDto(BaseModel):
    parameter: ParameterDto
    type: Literal[ContractType.TransferContract]
