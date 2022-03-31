import pathlib
from os import environ

from dotenv import load_dotenv

from runner.create_price_aggregator import create_price_aggregator
from runner.eth import ETHRunner, ETHRunnerCreateOptions

if __name__ == "__main__":
    load_dotenv()

    cwd = pathlib.Path(__file__).parent.resolve()

    price_aggregator = create_price_aggregator()

    runner = ETHRunner.create(ETHRunnerCreateOptions(
        input_file_path="./data/eth_0x228F5fFe4BFFE42278d50563B728aF83C36bd1A0.csv",
        output_file_path="./data/out/eth_parsed_out_0x228F5fFe4BFFE42278d50563B728aF83C36bd1A0.csv",
        trx_list_file_path="./data/cache/eth_trx_list.txt",
        price_aggregator=price_aggregator,
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_INFURA_RPC_ENDPOINT")))

    runner.run()
    runner.save_results()
