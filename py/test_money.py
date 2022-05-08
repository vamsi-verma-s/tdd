import unittest
from money import Money
from portfolio import Portfolio
from bank import Bank

class TestMoney(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        self.bank.addExchangeRate("EUR", "USD", 1.2)
        self.bank.addExchangeRate("USD", "KRW", 1100)

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
        self.assertEqual(fifteenDollars, portfolio.evaluate(self.bank, 'USD'))

    def testAdditonOfDollarsAndEuros(self):
        fiveDollars = Money(5, 'USD')
        tenEuros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, 'USD')
        self.assertEqual(expectedValue, portfolio.evaluate(self.bank, 'USD'))

    def testAdditionOfDollarsAndWon(self):
        oneDollar = Money(1, 'USD')
        elevenHundredWons = Money(1100, 'KRW')
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWons)
        expectedValue = Money(2200, 'KRW')
        self.assertEqual(expectedValue, portfolio.evaluate(self.bank, 'KRW'))

    def testAdditionWithMultipleMissingExchangeRates(self):
        oneDollar = Money(1, 'USD')
        oneEuro = Money(1, 'EUR')
        oneWon = Money(1, 'KRW')
        portfolio = Portfolio()
        portfolio.add(oneDollar, oneEuro, oneWon)
        with self.assertRaisesRegex(
            Exception,
            "Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]",
        ):
            portfolio.evaluate(self.bank, "Kalganid")

    def testConversion(self):
        bank = Bank()
        bank.addExchangeRate('EUR', 'USD', 1.2)
        tenEuros = Money(10, 'EUR')
        self.assertEqual(bank.convert(tenEuros, 'USD'), Money(12, 'USD'))

    def testConversionWithMissingExchangeRates(self):
        bank = Bank()
        tenEuros = Money(10, 'EUR')
        with self.assertRaisesRegex(Exception, "EUR->Kalganid"):
            bank.convert(tenEuros, 'Kalganid')

if __name__ == '__main__':
    unittest.main()