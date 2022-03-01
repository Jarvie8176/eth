from typing import Literal

from pydantic import BaseModel

from dto.TronGrid.contractType import ContractType


class ParameterValueDto(BaseModel):
    amount: int
    asset_name: str
    owner_address: str
    to_address: str


class ParameterDto(BaseModel):
    value: ParameterValueDto
    type_url: str


class TransferAssetContractDto(BaseModel):
    parameter: ParameterDto
    type: Literal[ContractType.TransferAssetContract]
