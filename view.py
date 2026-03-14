from products import *


def view():
    print("-" * 34)
    for product in products:
        print(f"Name : {product['name']}")
        print(f"Price : {product['price']:,.0f}")
        print(f"Amount : {product['amount']}")
        print(f"Total : {product['total']:,.0f}")