import pytest
from pricing.checkout import Checkout

def test_item_price():
    checkout = Checkout({'A': {'name':'A','unit_price':20,'special_qty':3,'special_price':50}})
    assert 170 == checkout.item_price('A', '10')

    checkout = Checkout({'B': {'name': 'B', 'unit_price':30}})
    assert 150 == checkout.item_price('B', '5')

    checkout = Checkout({'B': {'name': 'B', 'unit_price':30}})
    with pytest.raises(KeyError):
        checkout.item_price('A', '5')

    checkout = Checkout({'B': {'name': 'B', 'unit_price':30}})
    with pytest.raises(ValueError):
        checkout.item_price('B', 'not a number')

    checkout = Checkout({'B': {'name': 'B', 'unit_price':30}})
    assert 0 == checkout.item_price('B', '')

    checkout = Checkout({'B': {'name': 'B', 'unit_price':30}})
    assert 60 == checkout.item_price('B', 2)

def test_calc_price():
    checkout = Checkout({'A': {'name':'A','unit_price':20,'special_qty':3,'special_price':50}, 'B': {'name': 'B', 'unit_price':30}})
    assert 320 == checkout.calc_price({'A': '10', 'B': '5'})

    checkout = Checkout({'A': {'name':'A','unit_price':20,'special_qty':3,'special_price':50}, 'B': {'name': 'B', 'unit_price':30}})
    with pytest.raises(KeyError):
        checkout.calc_price({'A': '10', 'C': '5'})

