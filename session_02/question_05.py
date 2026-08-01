s = float(input('please enter the distance traveled in kilometers :'))
if s < 2 :
    print('The fixed fare is 20000 Tomans.')
else:
    s = s - 2
    m = (s * 5000) + 20000
    a = int(m)
    print('The fixed fare is', int(m) , 'Tomans.')
    