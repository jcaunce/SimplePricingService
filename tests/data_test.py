import pytest
from pricing.data import Prices

def test_test_data():
    prices = Prices()

    valid_data = [{'name': 'A', 'unit_price': 1}, {'name': 'B', 'unit_price': 1, 'special_qty': 2, 'special_price': 3}]
    assert prices._test_data(valid_data)

    data = {'name': 'A', 'unit_price': 1}
    with pytest.raises(Exception):
        prices._test_data(data)

    data = [{'unit_price': 1}]
    with pytest.raises(Exception):
        prices._test_data(data)

    data = [{'name': 'A'}]
    with pytest.raises(Exception):
        prices._test_data(data)

    data = [{'name': 1, 'unit_price': 1}]
    with pytest.raises(Exception):
        prices._test_data(data)

    data = [{'name': 'A', 'unit_price': '1'}]
    with pytest.raises(Exception):
        prices._test_data(data)

    data = [{'name': 'B', 'unit_price': 1, 'special_qty': 2}]
    with pytest.raises(Exception):
        prices._test_data(data)

    data = [{'name': 'B', 'unit_price': 1, 'special_qty': '2', 'special_price': 3}]
    with pytest.raises(Exception):
        prices._test_data(data)

    data = [{'name': 'B', 'unit_price': 1, 'special_qty': 2, 'special_price': '3'}]
    with pytest.raises(Exception):
        prices._test_data(data)

