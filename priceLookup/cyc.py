from priceLookup.yahoo_finance import YahooPriceLookup


class CYCPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "CYC"
