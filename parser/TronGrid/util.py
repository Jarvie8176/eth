import json
from os import path
from typing import List

from dto.TronGrid.transaction import TrxDto
from dto.parsedTrx import ParsedTrx
from parser.TronGrid.defn_parser import TronGrid_parser_lookup


def prepare_parse_result(test_file_name: str) -> List[ParsedTrx]:
    payload_file = path.splitext(test_file_name)[0] + ".payload.txt"
    with open(payload_file, "r") as f:
        trx_data = json.loads(f.read())

    trx = TrxDto(**trx_data)
    parser = TronGrid_parser_lookup.find_parser(trx)
    return parser.parse(trx)
