from priceLookup.yahoo_finance import YahooPriceLookup


class MGOOGLPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "mGOOGL"
