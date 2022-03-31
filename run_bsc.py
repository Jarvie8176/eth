import pathlib
from os import environ

from dotenv import load_dotenv

from parser.Infura.defn_parser import Infura_parser_lookup
from runner.create_price_aggregator import create_price_aggregator
from runner.eth import ETHRunner, ETHRunnerCreateOptions

if __name__ == "__main__":
    load_dotenv()

    cwd = pathlib.Path(__file__).parent.resolve()

    Infura_parser_lookup.update_major_currency("BNB")

    price_aggregator = create_price_aggregator()

    runner = ETHRunner.create(ETHRunnerCreateOptions(
        input_file_path="./data/bsc_0x228f5ffe4bffe42278d50563b728af83c36bd1a0.csv",
        output_file_path="./data/out/bsc_parsed_out_0x228f5ffe4bffe42278d50563b728af83c36bd1a0.csv",
        trx_list_file_path="./data/cache/bsc_trx_list.txt",
        price_aggregator=price_aggregator,
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_BIFINANCE_RPC_ENDPOINT")))

    runner.run()
    runner.save_results()
