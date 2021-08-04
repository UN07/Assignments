# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# CODE CELL
# PROBLEM 1

def get_product(code):

    return products[code]

get_product("americano")

# CODE CELL
# PROBLEM 2

def get_property(code, property):

    return products[code][property]

get_property("dalgona", "price")

# CODE CELL
# PROBLEM 3

def main():
    with open('receipt.txt', 'w') as r:
        r.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')
        customer_order = {}
        total = 0
        tracker = {'americano' : 0,
                    'brewedcoffee' : 0,
                    'cappuccino' : 0,
                    'dalgona' : 0,
                    'espresso' : 0,
                    'frappuccino' : 0,}
        while True:
            product = str(input("Product and quantity (product, quantity): "))

            if product == "/":
                break
            else:
                code, quantity = product.split(",")
                quantity = int(quantity)
                tracker[code] += quantity
                subtotal = get_property(code,"price") * tracker[code]
                total += get_property(code,"price") * quantity
                order = products[code]["name"]
                customer_order.update({code : {'order' : order, 'subtotal' : subtotal, 'quantity' : tracker[code]}})

        customer_order = dict(sorted(customer_order.items()))

        for i in customer_order:
            r.write(f'''
{i}\t\t{customer_order[i]['order']}\t\t{customer_order[i]['quantity']}\t\t\t\t\t\t{customer_order[i]['subtotal']}
''')

        r.write(f'''
Total:
{total}
==''')


main()
