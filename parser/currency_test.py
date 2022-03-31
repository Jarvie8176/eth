from parser.currency import Currency


def test_to_readable_value() -> None:
    currency = Currency(decimal_places=0, name="", unit="", contract_address="")
    assert currency.to_readable_value("0") == "0"
    assert currency.to_readable_value("1") == "1"
    assert currency.to_readable_value("12") == "12"

    currency = Currency(decimal_places=1, name="", unit="", contract_address="")
    assert currency.to_readable_value("0") == "0"
    assert currency.to_readable_value("1") == "0.1"
    assert currency.to_readable_value("10") == "1.0"
    assert currency.to_readable_value("12") == "1.2"

    currency = Currency(decimal_places=3, name="", unit="", contract_address="")
    assert currency.to_readable_value("0") == "0"
    assert currency.to_readable_value("1") == "0.001"
    assert currency.to_readable_value("12") == "0.012"
    assert currency.to_readable_value("123") == "0.123"
    assert currency.to_readable_value("1234") == "1.234"
    assert currency.to_readable_value("12345") == "12.345"

    currency = Currency(decimal_places=6, name="", unit="", contract_address="")
    assert currency.to_readable_value("2363782943") == "2363.782943"


def test() -> None:
    currency = Currency(decimal_places=18, name="", unit="", contract_address="")
    assert currency.to_readable_value("22812479999873264") == "0.022812479999873264"
