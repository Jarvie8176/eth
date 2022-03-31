import pathlib
from os import path, environ

from runner.create_price_aggregator import create_price_aggregator
from runner.eth import ETHRunner, ETHRunnerCreateOptions


def test() -> None:
    cwd = pathlib.Path(__file__).parent.resolve()

    price_aggregator = create_price_aggregator()

    runner = ETHRunner.create(ETHRunnerCreateOptions(
        input_file_path=path.join(cwd, "../data/test_fixture/eth_0x228F5fFe4BFFE42278d50563B728aF83C36bd1A0.csv"),
        output_file_path=path.join(cwd, "../data/out/e2e_test_eth_out.csv"),
        trx_list_file_path=path.join(cwd, "../data/test_fixture/e2e_test_eth_trx_list.txt"),
        price_aggregator=price_aggregator,
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_INFURA_RPC_ENDPOINT")))

    runner.run()
    runner.save_results()
    result = runner.to_dict()

    assert len(result.get("parsed_trxs")) == 65  # type: ignore
    assert len(result.get("failed_trxs")) == 120  # type: ignore

    # todo: check output file hash
