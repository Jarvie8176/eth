from enum import Enum


class ContractType(str, Enum):
    TransferAssetContract = "TransferAssetContract"
    TransferContract = "TransferContract"
    TriggerSmartContract = "TriggerSmartContract"
