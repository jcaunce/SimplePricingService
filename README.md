# SimplePricingService

This is an online checkout pricing service that allows a user to add multiple
items then displays the total price. It uses the pricing rules provided by the
json service at http://api.myjson.com/bins/gx6vz.

Whenever `special_qty` of an item are added, `special_price` is used for that
quantity. I've assumed that a user can add as many multiples of `special_qty` as
they like each for `special_price`, however any additional items have
`unit_price`.

## Installation

This service runs on Python 3 and Flask.

### virtualenv

You will probably want to run SimplePricingService in virtualenv, which allows
you to have multiple side-by-side Python installations. Instructions on how to
use virtualenv are at http://flask.pocoo.org/docs/0.12/installation/#virtualenv.

### setuptools

From the project directory, you can install SimplePricingService as a Python module run:

`$ python setup.py install`

### Running the service

The bash shell script will then be able to run the service (in Linux):

`$ ./pricing.sh`

Once it's up and running, you can access it at:

`http://127.0.0.1:5000`

## Testing

The unit tests can be run with the command:

`$ python setup.py test`
