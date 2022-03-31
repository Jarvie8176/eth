from typing import List, Optional

from dto.Infura.transaction import TrxDto, TrxLogDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from models.exceptions import TransactionSkipped
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status

class Parser(InfuraParser):
    """
    default parser of "deposit", method_id: "0xe2bbb158"
    """

    def can_handle(self, trx: TrxDto) -> bool:
        return trx.details.method_id in ["0xe2bbb158", "0x068f536f", "0xb6b55f25", "0xd0e30db0", "0xd2d0e066"]

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = self.find_in_trx_log(trx)

        if not in_trx_log:
            raise ValueError("cannot find transaction log of in event (no dividend found)")

        in_payload = TrxPayload(value=str(int(in_trx_log.data, 0)),
                                value_major=None,
                                currency=Infura_currency_lookup.contract_address_to_currency(in_trx_log.address))
        out_payload = None
        fee_payload = TrxPayload(value=trx.trx_fee,
                                 value_major=trx.trx_fee,
                                 currency=self.major_currency)

        return [ParsedTrx(trx_id=trx.trx_id,
                          url=trx.url,
                          type=ParsedTrxType.Dividend,
                          status=parse_status(trx.receipt.status),
                          timestamp=trx.timestamp,
                          major_currency=self.major_currency,
                          in_payload=in_payload,
                          out_payload=out_payload,
                          fee_payload=fee_payload)]

    def find_in_trx_log(self, trx: TrxDto) -> Optional[TrxLogDto]:
        if trx.trx_id == "0x957d0e6b1b6cdf01b2da84af54eace73e983a43677bddd648edb529b4c2eca19":
            raise TransactionSkipped("special case: no dividend")
        return self.find_first_transfer_in_log(trx)
