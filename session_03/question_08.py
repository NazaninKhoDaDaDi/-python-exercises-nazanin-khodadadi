a = int(input('Enter your account balance :'))
b = int(input('Enter the withdrawal amount :'))

if b <= 0 :
        print('Error')
elif a >= b :
    c = a - b
    print('operation completed.')
    print('Acoount balance : ' , c)
elif a < b :
        print('Insufficient account balance.')
