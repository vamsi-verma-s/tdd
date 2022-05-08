from money import Money
from functools import reduce
import operator

class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, bank, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                convertedMoney = bank.convert(m, currency)
                total += convertedMoney.amount
            except Exception as ke:
                failures.append(ke)

        if not failures:
            return Money(total, currency)

        failureMessage = ",".join(f.args[0] for f in failures)
        raise Exception('Missing exchange rate(s):[' + failureMessage + ']')