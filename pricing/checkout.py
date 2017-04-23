''' A class to calculate the price of a list of items '''
class Checkout():

    ''' Initialise with the price data from the json service '''
    def __init__(self, price_data):
        if type(price_data) != dict:
            raise
        for key, value in price_data.items():
            if type(key) != str: raise
            if type(value) != dict: raise
        # I'm assuming beyond this that the price_data is valid

        self.price_data = price_data

    ''' Calulate the total price of all the items '''
    def calc_price(self, items):
        price = 0
        for name, qty in items.items():
            price = price + self.item_price(name, qty)
        return price

    ''' Calculate the price of a quantity of one item '''
    def item_price(self, name, qty_str):
        if type(qty_str) == int:
            qty = qty_str
        elif qty_str == '':
            qty = 0
        else:
            qty = int(qty_str)

        item_data = self.price_data[name]

        if 'special_qty' in item_data:
            special_bundles = int(qty / item_data['special_qty'])
            extra = qty % item_data['special_qty']
            return item_data['special_price'] * special_bundles + item_data['unit_price'] * extra
        else:
            return item_data['unit_price'] * qty

