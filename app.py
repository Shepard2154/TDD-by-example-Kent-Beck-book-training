from abc import ABC
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


class Bank:
    exchange_rate = {}

    def add_rate(self, from_currency: str, to_currency: str, rate: float):
        self.exchange_rate[(from_currency, to_currency,)] = rate

    def exchange(
        self,
        source_money: Money,
        target_currency: str,
    ) -> Money:
        if source_money.currency == target_currency:
            return source_money
        return Money(
               source_money.amount * self.exchange_rate[
                   (source_money.currency, target_currency,)
                   ],
               target_currency,

        )
