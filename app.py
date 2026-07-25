from typing import Self


class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __mul__(self, multiplier: float):
        return Money(self.amount * multiplier, self.currency)

    def __add__(self, other: Self):
        return Money(self.amount + other.amount, self.currency)

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

