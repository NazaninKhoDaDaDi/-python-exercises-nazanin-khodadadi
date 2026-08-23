import random

while True:
    a = random.choice(['Sang' , 'Kaghaz' , 'Gheychi'])
    b = input('Please enter Sang,Kaghaz, Gheychi (or Exit) :')
    
    if b=='Exit':
        break
    if b !='Sang' and b != 'Kaghaz' and b != 'Gheychi':
        print('Invalid input.Please try again')
        continue
    
    if a == b:
        print('computer choise : ' , a)
        print('Mosavi')
    elif b == 'Sang' and a =='Gheychi':
        print('computer choise : ' , a)
        print('Bordi')
    elif b == 'Kaghaz' and a =='Sang':
        print('computer choise : ' , a)
        print('Bordi')
    elif b == 'Gheychi'and a == 'Kaghaz':
        print('computer choise : ' , a)
        print('Bordi')
    else :
        print('computer choise : ' , a)
        print('Bakhti')