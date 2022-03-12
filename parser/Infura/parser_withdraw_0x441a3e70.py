from typing import List, Optional

from dto.Infura.transaction import TrxDto, TrxLogDto
from dto.parsedTrx import ParsedTrx, TrxPayload, ParsedTrxType
from models.exceptions import TransactionSkipped
from parser.Infura.parser_base import InfuraParser
from parser.Infura.defn_currency import Infura_currency_lookup
from parser.Infura.defn_status import parse_status


class Parser(InfuraParser):
    """
    default parser of "withdraw", method_id: "0x441a3e70" (withdraw with dividend)
    """

    def can_handle(self, trx: TrxDto) -> bool:
        if trx.details.method_id == "0x441a3e70":
            if len(trx.receipt.logs) <= 2:
                raise TransactionSkipped("withdraw only, no dividend")
            return True

    def parse(self, trx: TrxDto) -> List[ParsedTrx]:
        in_trx_log = self.find_in_trx_log(trx)

        if not in_trx_log:
            raise ValueError("cannot find transaction log of in event")

        in_payload = TrxPayload(value=str(int(in_trx_log.data, 0)),
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
        first_log = trx.receipt.get_log_by_index(0)
        transfer_topic = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"

        # special case: https://bscscan.com/tx/0x13d47ffc2a60d8028dcf4da046fe898542b3fa2ea475c546e7a0919f6a19814a
        MoMoKEY_addr = "0x85c128ee1feeb39a59490c720a9c563554b51d33"
        if int(first_log.topics[0], 0) == int(transfer_topic, 0) and int(first_log.address, 0) == int(MoMoKEY_addr, 0):
            return first_log

        # special case: https://bscscan.com/tx/0x30b2a2afc09159dc5269533c017279fdad985e8c64457540db10d782fdc25ec9
        SHD_addr = "0x5845cd0205b5d43af695412a79cf7c1aeddb060f"
        if int(first_log.topics[0], 0) == int(transfer_topic, 0) and int(first_log.address, 0) == int(SHD_addr, 0):
            return first_log

        return self.find_first_transfer_in_log(trx)
