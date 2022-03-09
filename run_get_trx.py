import sys
from explorerClient.eth import ETHExplorerClient

if __name__ == "__main__":
    client = ETHExplorerClient.create(rpc_endpoint="https://mainnet.infura.io/v3/5b074910bb1d4b8f883ca53b0a8f0423")
    print(client.get_transaction(sys.argv[1]).json())
