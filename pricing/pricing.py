from flask import Flask, render_template, request
from .data import Prices
from .checkout import Checkout

app = Flask(__name__)

prices = Prices()
checkout = Checkout(prices.price_data_dict())

@app.route('/')
def hello_world():
    return render_template('form.html', data=prices.price_data)

@app.route('/checkout', methods=['POST'])
def do_checkout():
    price = checkout.calc_price(request.form)
    return render_template('checkout.html', price=price)
