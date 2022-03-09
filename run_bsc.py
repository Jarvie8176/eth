from os import environ

from dotenv import load_dotenv

from parser.Infura.defn_parser import Infura_parser_lookup
from runner.eth import ETHRunner, ETHRunnerCreateOptions

if __name__ == "__main__":
    load_dotenv()

    cwd = "."

    Infura_parser_lookup.update_major_currency("BNB")

    runner = ETHRunner.create(ETHRunnerCreateOptions(
        input_file_path="./data/bsc_0x228f5ffe4bffe42278d50563b728af83c36bd1a0.csv",
        trx_list_file_path="./data/cache/bsc_trx_list.txt",
        eth_price_data_file_path="./resources/historicalPrice/Bitfinex_ETHUSD_1h.csv",
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_BIFINANCE_RPC_ENDPOINT")))

    runner.run()
