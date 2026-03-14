products = []

def new_product():
    product_name = input("Enter product name: ")
    running = True
    while running:
        try:
            price = int(input("Enter the unit price of the product: ").replace(",","").replace(".",""))
            running = False
        except ValueError:
            print("wrong. just numbers")

    running = True
    while running:
        try:
            amount = int(input("Enter quantity: "))
            running = False
        except ValueError:
            print("wrong. just numbers")

    total = price * amount

    save_product = {
        "name": product_name,
        "price": price,
        "amount": amount,
        "total": total
    }

    products.append(save_product)


