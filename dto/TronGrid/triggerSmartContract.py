from typing import Literal

from pydantic import BaseModel

from dto.TronGrid.contractType import ContractType


class ParameterValueDto(BaseModel):
    data: str
    owner_address: str
    contract_address: str


class ParameterDto(BaseModel):
    value: ParameterValueDto
    type_url: str


class TriggerSmartContractDto(BaseModel):
    parameter: ParameterDto
    type: Literal[ContractType.TriggerSmartContract]
