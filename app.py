class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency


class Dollar(Money):
    pass


class Franc(Money):
    pass
