from priceLookup.yahoo_finance import YahooPriceLookup


class MDXPriceLookup(YahooPriceLookup):
    @property
    def unit(self) -> str:
        return "MDX"
