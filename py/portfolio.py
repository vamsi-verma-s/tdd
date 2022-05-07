from money import Money
from functools import reduce
import operator

class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = reduce(operator.add, map(lambda m: m.amount, self.moneys))
        return Money(total, currency)