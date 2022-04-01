import pathlib
from os import environ, path

from dotenv import load_dotenv

from runner.create_price_aggregator import create_price_aggregator
from runner.tron import TronGridRunner, TronGridRunnerCreateOptions

if __name__ == "__main__":
    load_dotenv()

    cwd = pathlib.Path(__file__).parent.resolve()

    price_aggregator = create_price_aggregator()

    # runner = TronGridRunner.create(TronGridRunnerCreateOptions(
    #     input_file_path=path.join(cwd, "./data/tron_TJVx5aV1Ajb9TBog7XVSakf5xZb3pMbAL8.csv"),
    #     output_file_path=path.join(cwd, "./data/out/tron_parsed_out_TJVx5aV1Ajb9TBog7XVSakf5xZb3pMbAL8.csv"),
    #     trx_list_file_path=path.join(cwd, "./data/cache/tron_trx_list.txt"),
    #     price_aggregator=price_aggregator,
    #     api_client_rpc_endpoint=environ.get("APP_API_CLIENT_TRONGRID_RPC_ENDPOINT")))

    # runner = TronGridRunner.create(TronGridRunnerCreateOptions(
    #     input_file_path=path.join(cwd, "./data/tron_TLkjSwb7Bb5XSPaJ8DPSf3Qak6qq5Kkd91.csv"),
    #     output_file_path=path.join(cwd, "./data/out/tron_parsed_out_TLkjSwb7Bb5XSPaJ8DPSf3Qak6qq5Kkd91.csv"),
    #     trx_list_file_path=path.join(cwd, "./data/cache/tron_trx_list.txt"),
    #     price_aggregator=price_aggregator,
    #     api_client_rpc_endpoint=environ.get("APP_API_CLIENT_TRONGRID_RPC_ENDPOINT")))

    runner = TronGridRunner.create(TronGridRunnerCreateOptions(
        input_file_path=path.join(cwd, "./data/tron_TKN9QU6PuTRaUCaT3hwjppNdAQDcz3tuM5.csv"),
        output_file_path=path.join(cwd, "./data/out/tron_parsed_out_TKN9QU6PuTRaUCaT3hwjppNdAQDcz3tuM5.csv"),
        trx_list_file_path=path.join(cwd, "./data/cache/tron_trx_list.txt"),
        price_aggregator=price_aggregator,
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_TRONGRID_RPC_ENDPOINT")))




    runner.run()
    runner.save_results()
