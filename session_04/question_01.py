import random
a = random.randint(1, 100)

while True:
    b = int(input('Please enter your guess between 1 and 100 :'))
    if b > a :
        print('sorry,Please choose a smaller number')
        continue
    elif b < a :
        print('sorry,Please choose a larger number')
        continue
    elif b == a :
        print('Success.tour guess is correct.')
        break
