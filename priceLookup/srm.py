from priceLookup.yahoo_finance import YahooPriceLookup


class SRMPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "SRM"
