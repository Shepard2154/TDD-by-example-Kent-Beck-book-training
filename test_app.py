from app import Bank, Money


def test_multiplication():
    five = Money.dollar(5)
    assert five * 2 == Money.dollar(10)
    assert five * 3 == Money.dollar(15)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) != Money.dollar(5)


def test_currency():
    assert 'USD' == Money.dollar(1).currency
    assert 'CHF' == Money.franc(1).currency


def test_simple_addition():
    five = Money.dollar(5)
    bank = Bank()
    reduced = bank.exchange(five + five, 'USD')
    assert Money.dollar(10) == reduced


def test_mixed_addition():
    five = Money.dollar(5)
    four = Money.franc(4)
    bank = Bank()
    bank.add_rate(
         from_currency='CHF',
         to_currency='USD',
         rate=0.5,
    ) # 1 USD = 2 CHF
    reduced = bank.exchange(four, 'USD') + five
    assert Money.dollar(7) == reduced
