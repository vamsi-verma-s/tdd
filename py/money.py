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

    def __str__(self) -> str:
        return f'{self.amount} {self.currency}'

    def __repr__(self) -> str:
        return f'Money({self.amount}, {self.currency})'