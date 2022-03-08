from os import environ

from dotenv import load_dotenv


# RPC_ENDPOINT = "https://mainnet.infura.io/v3/5b074910bb1d4b8f883ca53b0a8f0423"
# provider = Web3.HTTPProvider(RPC_ENDPOINT)
# w3 = Web3(provider)
# print(w3.eth.getTransaction("0x8127bde071aa22c15ff4139e87e3a8abc2e0f2269a5972b06c73b5b66019e156"))
# print("=====")
# print(w3.eth.getTransactionReceipt("0x8127bde071aa22c15ff4139e87e3a8abc2e0f2269a5972b06c73b5b66019e156"))
from runner.eth import ETHRunner, ETHRunnerCreateOptions

if __name__ == "__main__":
    # client = ETHExplorerClient.create(rpc_endpoint="https://mainnet.infura.io/v3/5b074910bb1d4b8f883ca53b0a8f0423")
    # print(client.get_transaction("0x6ea2ccc2485022bdd3cbefa34c200efb6a3b52e53d55105426e375df6755db08").json())

    load_dotenv()

    cwd = "."

    runner = ETHRunner.create(ETHRunnerCreateOptions(
        input_file_path="./data/test_fixture/eth_0x228F5fFe4BFFE42278d50563B728aF83C36bd1A0.csv",
        trx_list_file_path="./data/cache/eth_trx_list.txt",
        eth_price_data_file_path="./resources/historicalPrice/Bitfinex_ETHUSD_1h.csv",
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_RPC_ENDPOINT")))

    runner.run()
