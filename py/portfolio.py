from money import Money
from functools import reduce
import operator

class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def __convert(self, money, currency):
        if money.currency == currency:
            return money.amount
        return money.amount * self._eur_to_usd

    def evaluate(self, currency):
        total = reduce(operator.add, map(lambda m: self.__convert(m, currency), self.moneys))
        return Money(total, currency)