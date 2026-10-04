orders = [
    ("Ali", "Laptop"),
    ("Sara", "Phone"),
    ("Ali", "Phone"),
    ("Reza", "Laptop"),
    ("Sara", "Laptop"),
    ("Ali", "Tablet"),
    ("Reza", "Phone")
]

customer_orders = {}

for i in orders:
    if i[0] in customer_orders:
        customer_orders[i[0]].append(i[1])
    else:
        customer_orders[i[0]] = [i[1]]

print('{')

for i in customer_orders:
    print('"', i, '":', customer_orders[i])

print('}')