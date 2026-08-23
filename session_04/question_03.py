a = input('Please enetr your Password:')

if len(a) == 8:
    first = a[0 : 4]
    last = a[4 : 8]
    
    if  not first.isdigit() and last.isdigit():
        print('Valid')
    else:
        print('Invalid.')
        print('First 4: Lettesr, Last 4: numbers')
else:
    print('Invalid.Enter a password with a length of 8.')
