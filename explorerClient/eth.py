from __future__ import annotations

from typing import List, Any

from loguru import logger

from dto.Infura.transaction import TrxDto, TrxDetailsDto, TrxBlockDto, TrxReceiptDto
import requests as requests


class ETHExplorerClient:
    """
    ETH network explorer client that parses wallet transactions
    """

    def __init__(self, rpc_endpoint: str):
        self.rpc_endpoint = rpc_endpoint

    def _send_transaction_request(self, method: str, params: List[Any]) -> requests.Response:
        url = self.rpc_endpoint
        payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        return requests.request("POST", url, json=payload, headers=headers)

    def get_transaction_details(self, trx_id: str) -> TrxDetailsDto:
        payload = self._send_transaction_request(params=[trx_id], method="eth_getTransactionByHash").json()
        return TrxDetailsDto(**payload.get("result"))

    def get_transaction_receipt(self, trx_id: str) -> TrxReceiptDto:
        payload = self._send_transaction_request(params=[trx_id], method="eth_getTransactionReceipt").json()
        return TrxReceiptDto(**payload.get("result"))

    def get_transaction_block(self, block_id: str) -> TrxBlockDto:
        payload = self._send_transaction_request(params=[block_id, False], method="eth_getBlockByHash").json()
        return TrxBlockDto(**payload.get("result"))

    def get_transaction(self, trx_id: str) -> TrxDto:
        # todo: error handling of jsonrpc response
        # e.g. {"jsonrpc":"2.0","id":1,"error":{"code":-32602,"message":"missing value for required argument 1"}}

        details = self.get_transaction_details(trx_id)
        receipt = self.get_transaction_receipt(trx_id)
        block = self.get_transaction_block(receipt.blockHash)
        logger.debug(f"transaction fetched: {trx_id}")
        return TrxDto(details=details, receipt=receipt, block=block)

    @staticmethod
    def create(rpc_endpoint: str) -> ETHExplorerClient:
        """
        :param rpc_endpoint: from https://infura.io/dashboard
        :return:
        """

        return ETHExplorerClient(rpc_endpoint=rpc_endpoint)
