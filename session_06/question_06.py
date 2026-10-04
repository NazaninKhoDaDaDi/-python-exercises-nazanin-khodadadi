sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)

customer_sales = {}
maximum = 0
maximum_name = ''
product_sales = {}
total = 0

for i in sales:
    if i[0] in customer_sales:
        customer_sales[i[0]] = customer_sales[i[0]] + i[2]
    else : 
        customer_sales[i[0]] = i[2]

for i in customer_sales:
    print(i, '->' , customer_sales[i])
    
print()

for i in customer_sales:
    if customer_sales[i] > maximum:
        maximum = customer_sales[i]
        maximum_name = i

print(maximum_name, '->', maximum)
print()

for i in sales:
    if i[1] in product_sales:
        product_sales[i[1]] = product_sales[i[1]] + 1
    else:
        product_sales[i[1]] = 1
for i in product_sales:
    print(i, '->' , product_sales[i])
    
for i in sales:
    total = total + i[2]
print()
print('Total sales:', total)