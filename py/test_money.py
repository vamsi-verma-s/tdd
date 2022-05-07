import unittest
from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        tenEuros = Money(10, 'EUR')
        twentyEuros = Money(20, 'EUR')
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivsion(self):
        originalMoney = Money(4002, 'KWR')
        expectedMoneyAfterDivision = Money(1000.5, 'KWR')
        self.assertEqual(expectedMoneyAfterDivision, originalMoney.divide(4))

    def testAddition(self):
        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')
        fifteenDollars = Money(15, 'USD')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate('USD'))

    def testAdditonOfDollarsAndEuros(self):
        fiveDollars = Money(5, 'USD')
        tenEuros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, 'USD')
        self.assertEqual(expectedValue, portfolio.evaluate('USD'))

    def testAdditionOfDollarsAndWon(self):
        oneDollar = Money(1, 'USD')
        elevenHundredWons = Money(1100, 'KRW')
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWons)
        expectedValue = Money(2200, 'KRW')
        self.assertEqual(expectedValue, portfolio.evaluate('KRW'))

if __name__ == '__main__':
    unittest.main()