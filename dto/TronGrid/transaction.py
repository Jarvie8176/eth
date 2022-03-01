from typing import Optional, List, Union

from loguru import logger
from typing_extensions import Annotated

from pydantic.fields import Field
from pydantic.main import BaseModel

from dto.TronGrid.event import EventDto
from dto.TronGrid.transferAssetContract import \
    TransferAssetContractDto
from dto.TronGrid.transferContract import TransferContractDto
from dto.TronGrid.triggerSmartContract import \
    TriggerSmartContractDto


class TrxInfoReceiptDto(BaseModel):
    net_fee: Optional[int]
    net_usage: Optional[int]


class TrxInfoDto(BaseModel):
    id: str
    fee: Optional[int]
    blockNumber: int
    blockTimeStamp: int
    receipt: TrxInfoReceiptDto


class TrxRetDto(BaseModel):
    contractRet: str


TrxRawDataContractDto = Annotated[Union[TransferAssetContractDto,
                                        TransferContractDto,
                                        TriggerSmartContractDto],
                                  Field(discriminator="type")]


class TrxRawDataDto(BaseModel):
    contract: List[TrxRawDataContractDto]
    ref_block_bytes: str  # int in str?
    ref_block_hash: str
    expiration: int  # in milliseconds
    fee_limit: Optional[int]
    timestamp: int  # in milliseconds


class TrxDetailsDto(BaseModel):
    ret: List[TrxRetDto]
    signature: List[str]
    txID: str
    raw_data: TrxRawDataDto
    raw_data_hex: str


class TrxDto(BaseModel):
    details: TrxDetailsDto
    info: TrxInfoDto
    events: EventDto

    @property
    def trx_id(self) -> str:
        return self.details.txID

    @property
    def status(self) -> str:
        return ", ".join([ret.contractRet for ret in self.details.ret])

    """
    returns the first contract in transaction, None if there is no contract
    """

    def get_contract(self) -> Optional[TrxRawDataContractDto]:
        contracts = self.details.raw_data.contract
        if len(contracts) == 0:
            logger.warning(f"no contract in trx: {self.trx_id}")
        if len(contracts) > 1:
            logger.warning(f"more than one contract in trx: {self.trx_id}")
        return contracts[0]
