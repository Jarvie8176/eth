import json
from typing import Dict, Iterable, IO, Tuple, List

import pandas as pd
import requests as requests
from loguru import logger
import csv

from aggregator.price import PriceAggregator
from dto.TronGrid.transaction import TrxInfoDto, TrxDetailsDto, TrxDto
from dto.parsedTrx import ParsedTrx
from models.exceptions import ParserNotFound
from parser.TronGrid.parserLookup import ParserLookup


def load_csv(file_path) -> Tuple[IO, Iterable[Dict]]:
    logger.debug("input file: {file_path}", file_path=file_path)
    file = open(file_path, 'r')
    input = csv.DictReader(file)
    return file, input


# def get_transaction_details(trx_id: str) -> TrxDetailsDto:
#     logger.debug("fetch trx details: {trx_id}", trx_id=trx_id)
#     url = "https://api.trongrid.io/wallet/gettransactionbyid"
#     payload = {"value": trx_id}
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json"
#     }
#     response = requests.request("POST", url, json=payload, headers=headers)
#     return TrxDetailsDto(**response.json())


def get_transaction_events(trx_id: str):  # todo: define dto
    logger.debug("fetch trx events: {trx_id}", trx_id=trx_id)
    url = f"https://api.trongrid.io/v1/transactions/{trx_id}/events"
    headers = {
        "Accept": "application/json",
    }
    response = requests.request("GET", url, headers=headers)
    result = response.json()
    result["tx_id"] = trx_id
    return result
    # return TrxDetailsDto(**response.json())


def get_transaction_info(trx_id: str) -> TrxInfoDto:
    logger.debug("fetch trx info: {trx_id}", trx_id=trx_id)
    url = "https://api.trongrid.io/wallet/gettransactioninfobyid"
    payload = {"value": trx_id}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return TrxInfoDto(**response.json())


def get_transaction(trx_id: str) -> TrxDto:
    trx_details = get_transaction_details(trx_id)
    trx_info = get_transaction_info(trx_id)
    return TrxDto(details=trx_details, info=trx_info)


def transaction_to_displayable(trx: TrxDto, events):
    if len(trx.details.raw_data.contract) > 1:
        raise Exception(f"more than 1 contract in trx: {trx.details.txID}")

    contract = trx.details.raw_data.contract[0]
    if contract.type != "TriggerSmartContract":
        logger.info(f"unsupported contract: {contract.type}")
        return

    event = find_event_by_trx(trx.details.txID, events)
    if not event:
        logger.info(f"no event found: {trx.details.txID}")
        return

    event_names = [evt_record["event_name"] for evt_record in event["data"]]
    if "Transfer" not in event_names:
        logger.info(f"no transfer event: {trx.details.txID}")
        return

    result = {
        "url": f"https://tronscan.org/#/transaction/{trx.details.txID}",
        "trx_id": trx.details.txID,
        "status": ", ".join([ret.contractRet for ret in trx.details.ret]),
        "timestamp": trx.info.blockTimeStamp,
        "type": contract.type,
        "method_id": contract.parameter.value.data[:8],
        "contract_address": contract.parameter.value.contract_address,
    }

    if "FAIL" in str(result["status"]):
        logger.info(f"transaction failed: {trx.details.txID}")
        return

    return result


def find_event_by_trx(trx_id, events):
    for event in events:
        if event.tx_id == trx_id:
            return event
    return None


if __name__ == "__main__":
    with open("data/trx_combined.txt", "r") as f_trx:
        transactions = map(lambda line: TrxDto(**json.loads(line)), f_trx.readlines())
        # print(list(transactions)[0].dict())

    parser_lookup = ParserLookup.create()

    parsed_trx: List[ParsedTrx] = []
    failed_trx: List[TrxDto] = []

    with open("data/trx_parsed_out.csv", "w") as f_out:
        for trx in transactions:
            try:
                parsed_trx.append(parser_lookup.find_parser(trx).parse(trx))
            except ParserNotFound:
                logger.info(f"cannot parse transaction: parser not found; {trx.trx_id}")
                failed_trx.append(trx)
            except Exception:
                logger.opt(exception=True).error(f"unexpected error: ({trx.trx_id}):")
                failed_trx.append(trx)

        price_aggregator = PriceAggregator.create(
            trx_price_data_file_path="./resources/historicalPrice/Bitfinex_TRXUSD_1h.csv")

        for i in parsed_trx:
            price_aggregator.update_price(i)
        pd.DataFrame.from_dict([i.to_dto().dict() for i in parsed_trx]).to_csv(f_out)

    # with open("data/output_events.txt", "r") as f_events:
    #     events = map(json.loads, f_events.readlines())
    #
    # with open("data/output.txt", "r") as f_trx:
    #     transactions = map(json.loads, f_trx.readlines())
    #
    # eventDtos = map(lambda event: EventDto(**event), events)
    # trxDtos = map(lambda trx: TrxDto(**trx), transactions)
    #
    # with open("data/trx_combined.txt", 'w') as f_out:
    #     for trx in trxDtos:
    #         event = find_event_by_trx(trx.trx_id, eventDtos)
    #         outDto = TrxDto(details=trx.details, info=trx.info, events=event)
    #         f_out.write(json.dumps(outDto.dict()) + "\n")

    # with open("output_events.txt", "r") as f_events:
    #     events = map(json.loads, f_events.readlines())
    #
    # with open("trx_parsed.txt", "r") as f:
    #
    #     lines = f.readlines()
    #     displayables = map(lambda line: transaction_to_displayable(TrxDto(**json.loads(line)), events), lines)
    #     displayables = list(filter(None, displayables))
    #
    #     with open("output.json", "w") as out_f:
    #         out_f.write(json.dumps(displayables))
    #
    # file_handle, input = load_csv("export.csv")
    # with open("output_events.txt", "w") as output_handle:
    #     for i in input:
    #         print(i)
    #         trx_id = i["hash"]
    #         try:
    #             events = get_transaction_events(trx_id)
    #             # trx = get_transaction(trx_id)
    #             # print(trx)
    #             output_handle.write(json.dumps(events) + "\n")
    #             # output_handle.write(json.dumps(trx.dict()) + "\n")
    #         except Exception as e:
    #             raise e

    # file_handle.close()
