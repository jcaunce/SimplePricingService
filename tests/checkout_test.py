import unittest
from pricing.checkout import Checkout

class TestCheckout(unittest.TestCase):
    def test_item_price(self):
        checkout = Checkout({'A': {'name':'A','unit_price':20,'special_qty':3,'special_price':50}})
        assert 170 == checkout.item_price('A', '10')

if __name__ == '__main__':
    unittest.main()
