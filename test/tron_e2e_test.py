import pathlib
from os import path, environ
from runner.create_price_aggregator import create_price_aggregator
from runner.tron import TronGridRunner, TronGridRunnerCreateOptions

from loguru import logger

environ.setdefault("LOGURU_LEVEL", "DEBUG")


def test() -> None:
    cwd = pathlib.Path(__file__).parent.resolve()

    price_aggregator = create_price_aggregator()

    runner = TronGridRunner.create(TronGridRunnerCreateOptions(
        input_file_path=path.join(cwd, "../data/test_fixture/tron_TJ7ozAvfPwxpNANWfMnAhVwGBYkwTjuscJ.csv"),
        output_file_path=path.join(cwd, "../data/out/e2e_test_tron_out.csv"),
        trx_list_file_path=path.join(cwd, "../data/cache/e2e_test_tron_trx_list.txt"),
        price_aggregator=price_aggregator,
        api_client_rpc_endpoint=environ.get("APP_API_CLIENT_TRONGRID_RPC_ENDPOINT")))

    runner.run()
    runner.save_results()
    result = runner.to_dict()

    assert len(result.get("parsed_trxs")) == 76  # type: ignore
    assert len(result.get("failed_trxs")) == 96  # type: ignore
