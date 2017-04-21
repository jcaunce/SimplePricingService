import requests

''' A class to get data from the json service and test that it is valid '''
class Prices():

    ''' Initialise the class by downloading the data from the json service '''
    def __init__(self):
        self.price_data = self._download_data()
        self._test_data(self.price_data)

    ''' Download the data from the json service. Raise an exception if it fails '''
    def _download_data(self):
        r = requests.get('http://api.myjson.com/bins/gx6vz')
        r.raise_for_status()
        return r.json()['prices']
        
    ''' Test that the data is valid '''
    def _test_data(self, data):
        if type(data) != list:
            raise Exception('Data is not a list')
        for item in data:
            if type(item) != dict:
                raise Exception('Data is not a dictionary')
            if 'name' not in item:
                raise Exception('Data does not contain a name')
            if type(item['name']) != str:
                raise Exception('Name is not a string')
            if 'unit_price' not in item:
                raise Exception('Data does not contain a unit price')
            if type(item['unit_price']) != int:
                raise Exception('Unit price is not an integer')
            if 'special_qty' in item:
                if 'special_price' not in item:
                    raise Exception('Data contains a special quantity, but not a special price')
                if type(item['special_qty']) != int:
                    raise Exception('Special quantity is not an integer')
                if type(item['special_price']) != int:
                    raise Exception('Special price is not an integer')
        return True

    ''' Returns the data in a dictionary that's easier to search '''
    def price_data_dict(self):
        data_dict = {}
        for data in self.price_data:
            data_dict[data['name']] = data
        return data_dict

