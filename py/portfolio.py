from money import Money
from functools import reduce
import operator

class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def __convert(self, money, currency):
        exchangeRates = {'EUR->USD': 1.2, 'USD->KRW': 1100}
        if money.currency == currency:
            return money.amount
        key = money.currency + '->' + currency
        return money.amount * exchangeRates[key]

    def evaluate(self, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failures.append(ke)

        if not failures:
            return Money(total, currency)

        failureMessage = ",".join(f.args[0] for f in failures)
        raise Exception('Missing exchange rate(s):[' + failureMessage + ']')