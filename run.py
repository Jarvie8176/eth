from os import environ

from dotenv import load_dotenv

from runner.eth import ETHRunner, ETHRunnerCreateOptions

if __name__ == "__main__":
    load_dotenv()

    cwd = "."

    runner = ETHRunner.create(ETHRunnerCreateOptions(
        input_file_path="./data/test_fixture/eth_0x228F5fFe4BFFE42278d50563B728aF83C36bd1A0.csv",
        trx_list_file_path="./data/cache/eth_trx_list.txt",
        eth_price_data_file_path="./resources/historicalPrice/Bitfinex_ETHUSD_1h.csv",
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_RPC_ENDPOINT")))

    runner.run()
