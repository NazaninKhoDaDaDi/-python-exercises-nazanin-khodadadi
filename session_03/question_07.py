a = input('Please enter the color1:')
b = input('Please enter the color2:')
c = input('Please enter the color3:')

if a==b and b==c:
    print('The three colors are equal.')
elif a==b or a==c or b==c :
    print('The two colors are equal.')
else:
    print('The colors are not the same.')
    