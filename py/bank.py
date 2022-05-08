from money import Money

class Bank:
    def __init__(self) -> None:
        self.exchangeRates = {}

    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        key = currencyFrom + '->' + currencyTo
        self.exchangeRates[key] = rate

    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aMoney.currency)
        
        key = aMoney.currency + '->' + aCurrency
        if key in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[key], aCurrency)

        raise Exception(key)