from app import Money


def test_multiplication():
    five = Money.dollar(5)
    assert five * 2 == Money.dollar(10)
    assert five * 3 == Money.dollar(15)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) == Money.franc(5)
    assert Money.franc(5) != Money.franc(6)
    assert Money.franc(5) != Money.dollar(5)


def test_currency():
    assert('USD', Money.dollar(1).currency)
    assert('CHF', Money.franc(1).currency)
