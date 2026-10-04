products = {
    "P01": ("Laptop", 1200, 5),
    "P02": ("Phone", 800, 0),
    "P03": ("Tablet", 500, 12),
    "P04": ("Mouse", 50, 25),
    "P05": ("Keyboard", 100, 0)
}

value = 0
maximum = 0
maximum_product = ''

print('Available products:')
for i in products:
    if products[i][2] > 0:
        print(products[i][0])

print()
print('Out of stock:')
for i in products:
    if products[i][2] == 0:
        print(products[i][0])

print()
for i in products:
    value = products[i][1] * products[i][2]
    print(products[i][0], '->', value)
print()
  
for i in products:
    value = products[i][1] * products[i][2]
    if value > maximum:
        maximum = value
        maximum_product = products[i][0]
print('Product with maximum inventory value:', maximum_product)
print('Maximum inventory value:', maximum)

    