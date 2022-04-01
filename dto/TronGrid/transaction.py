from datetime import datetime
from typing import Optional, List, Union, Any

from loguru import logger
from typing_extensions import Annotated

from pydantic.fields import Field
from pydantic.main import BaseModel

from tronapi import Tron

import pytz

from dto.TronGrid.event import TrxEventDto
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

tron = Tron()


class TrxRawDataDto(BaseModel):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        contract_size = len(self.contract)

        if contract_size != 1:
            logger.warning(f"contract size is not 1 ({contract_size})")

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

    @property
    def method_id(self) -> str:
        contract = self.get_contract()
        if not contract:
            logger.warning("transaction has no contract")
            return ""
        return contract.parameter.value.data[:8]

    def get_contract(self) -> Optional[TrxRawDataContractDto]:
        """
        returns the first contract in transaction, None if there is no contract
        :return: {TrxRawDataContractDto}
        """
        contracts = self.raw_data.contract
        if len(contracts) == 0:
            logger.warning(f"no contract in trx: {self.txID}")
            return None
        if len(contracts) > 1:
            logger.warning(f"more than one contract in trx: {self.txID}")
        return contracts[0]


class TrxDto(BaseModel):
    details: TrxDetailsDto
    info: TrxInfoDto
    events: TrxEventDto

    @property
    def trx_id(self) -> str:
        return self.details.txID

    @property
    def url(self) -> str:
        return f"https://tronscan.org/#/transaction/{self.trx_id}"

    @property
    def timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.info.blockTimeStamp, tz=pytz.UTC)

    @property
    def trx_fee(self) -> str:
        return str(self.info.fee)

    @property
    def status(self) -> str:
        return ", ".join([ret.contractRet for ret in self.details.ret])

    def get_contract(self) -> Optional[TrxRawDataContractDto]:
        return self.details.get_contract()

    def get_account_base58(self) -> str:
        """
        :return: account in base58 format
        """
        return tron.address.from_hex("41" + self.get_account_hex()[2:]).decode()

    def get_account_hex(self) -> str:
        """
        https://developers.tron.network/docs/account#account-address-format
        :return: account in hex format without the prefix "41"
        """
        return "0x" + self.details.raw_data.contract[0].parameter.value.owner_address[2:]
