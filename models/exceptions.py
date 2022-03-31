class InvalidTransaction(Exception):
    pass

class ParserNotFound(Exception):
    pass


class CurrencyNotFound(Exception):
    pass


class TransactionSkipped(Exception):
    pass


class TrxLogLengthNotMatch(Exception):
    pass
