i = int(input('enter a number between 0 and 23 : '))

if 6 <= i < 12 :
    print('Morning')
elif 12 <= i < 15 :
    print('Noon')
elif 15 <= i < 18 :
    print('Afternoon')
elif 0 <= i < 6 or 18 <= i <= 23:
    print('Night')
else:
    print('Invalid hour')
    
    