from __future__ import annotations

from loguru import logger

import requests as requests

from dto.TronGrid.event import TrxEventDto
from dto.TronGrid.transaction import TrxDto, TrxDetailsDto, TrxInfoDto


class TronGridExplorerClient:
    """
    TronGrid network explorer client that parses wallet transactions
    """

    def __init__(self, rpc_endpoint: str):
        self.rpc_endpoint = rpc_endpoint

    def _get_transaction_details(self, trx_id: str) -> TrxDetailsDto:
        # logger.debug(f"fetch trx details: {trx_id}")
        url = f"{self.rpc_endpoint}/wallet/gettransactionbyid"
        payload = {"value": trx_id}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        return TrxDetailsDto(**response.json())

    def _get_transaction_info(self, trx_id: str) -> TrxInfoDto:
        # logger.debug(f"fetch trx info: {trx_id}")
        url = f"{self.rpc_endpoint}/wallet/gettransactioninfobyid"
        payload = {"value": trx_id}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        return TrxInfoDto(**response.json())

    def _get_transaction_events(self, trx_id: str) -> TrxEventDto:
        # logger.debug(f"fetch trx events: {trx_id}")
        url = f"{self.rpc_endpoint}/v1/transactions/{trx_id}/events"
        headers = {
            "Accept": "application/json",
        }
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        result["tx_id"] = trx_id
        return TrxEventDto(**result)

    def get_transaction(self, trx_id: str) -> TrxDto:
        # todo: error handling of jsonrpc response
        # e.g. {"jsonrpc":"2.0","id":1,"error":{"code":-32602,"message":"missing value for required argument 1"}}

        logger.debug(f"fetching transaction: {trx_id}")
        trx_details = self._get_transaction_details(trx_id)
        trx_info = self._get_transaction_info(trx_id)
        trx_events = self._get_transaction_events(trx_id)
        logger.debug(f"transaction fetched: {trx_id}")
        return TrxDto(details=trx_details, info=trx_info, events=trx_events)

    @staticmethod
    def create(rpc_endpoint: str) -> TronGridExplorerClient:
        """
        :param rpc_endpoint: public node e.g. "https://api.trongrid.io"
        :return:
        """

        return TronGridExplorerClient(rpc_endpoint=rpc_endpoint)
