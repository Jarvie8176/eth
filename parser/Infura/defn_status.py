from dto.parsedTrx import ParsedTrxStatus


def parse_status(status: str) -> ParsedTrxStatus:
    if status == "0x1":
        return ParsedTrxStatus.Success

    raise ValueError(f"unknown status: {status}")
