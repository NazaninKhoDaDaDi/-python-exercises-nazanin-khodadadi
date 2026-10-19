customer = input('Enter customer name: ')
products = input('Enter products: ').split()

discount = int(input('Enter discount: '))
tax = int(input('Enter tax: '))
shipping = int(input('Enter shipping: '))


def process_order(customer, *products, **options):
    total = 0

    discount = options.get('discount', 0)
    tax = options.get('tax', 9)
    shipping = options.get('shipping', 0)

    prices = {
        'Laptop': 50000000,
        'Mouse': 500000,
        'Keyboard': 1500000
    }

    for i in products:
        total = total + prices[i]

    discount_amount = total * discount / 100
    price_after_discount = total - discount_amount

    tax_amount = price_after_discount * tax / 100

    final_price = price_after_discount + tax_amount + shipping

    result = {
        'customer': customer,
        'products': products,
        'discount': discount,
        'tax': tax,
        'shipping': shipping,
        'final_price': final_price
    }

    return result


print(process_order(
    customer,
    *products,
    discount=discount,
    tax=tax,
    shipping=shipping
))