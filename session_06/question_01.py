products = {
'laptop': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}

maximum = 0
product_max = ''

minimum = 999999
product_min = ''

total = 0

for i in products:
    if products[i] > maximum:
        maximum = products[i]
        product_max = i
print(product_max, '->', maximum)
print()      

for i in products:
    if products[i] < minimum:
        minimum = products[i]
        product_min = i
print(product_min, '->', minimum)
print()

for i in products:
    total = total + products[i]
    
average = total / len(products)
print('Average :', average)
print()

for i in products:
    if products[i] > 500 :
        print(i)
        
print()
print('Total : ' , total) 













