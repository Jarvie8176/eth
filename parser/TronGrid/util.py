import json
from os import path

from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrxDto
from parser.TronGrid.parserLookup import ParserLookup


def prepare_parse_result(test_file_name: str) -> ParsedTrxDto:
    payload_file = path.splitext(test_file_name)[0] + ".payload.txt"
    with open(payload_file, "r") as f:
        trx_data = json.loads(f.read())

    trx = TrxDto(**trx_data)
    parser = ParserLookup.create().find_parser(trx)
    return parser.parse(trx).to_dto()
