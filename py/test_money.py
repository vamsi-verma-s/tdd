import unittest

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency 
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount/divisor, self.currency)

    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount and self.currency == other.currency
        

class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        fiver = Money(5, 'USD')
        tenner = Money(10, 'USD')
        self.assertEqual(tenner, fiver.times(2))

    def testMultiplicationEuros(self):
        tenEuros = Money(10, 'EUR')
        twentyEuros = Money(20, 'EUR')
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivsion(self):
        originalMoney = Money(4002, 'KWR')
        expectedMoneyAfterDivision = Money(1000.5, 'KWR')
        self.assertEqual(expectedMoneyAfterDivision, originalMoney.divide(4))

if __name__ == '__main__':
    unittest.main()