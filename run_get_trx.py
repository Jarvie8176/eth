from os import environ

import sys
from dotenv import load_dotenv

from explorerClient.eth import ETHExplorerClient
from explorerClient.tron import TronGridExplorerClient

if __name__ == "__main__":
    load_dotenv()
    # client = ETHExplorerClient.create(rpc_endpoint=str(environ.get("APP_API_CLIENT_INFURA_RPC_ENDPOINT"))
    # client = ETHExplorerClient.create(rpc_endpoint=str(environ.get("APP_API_CLIENT_BIFINANCE_RPC_ENDPOINT")))
    client = TronGridExplorerClient.create(rpc_endpoint=str(environ.get("APP_API_CLIENT_TRONGRID_RPC_ENDPOINT")))
    print(client.get_transaction(sys.argv[1]).json())
