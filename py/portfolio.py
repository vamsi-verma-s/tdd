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
        total = reduce(operator.add, map(lambda m: self.__convert(m, currency), self.moneys))
        return Money(total, currency)