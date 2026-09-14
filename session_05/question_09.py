username = 'admin'
password = '193814'

c = 3

while c > 0 :
    user = input('Enter username: ')
    pas = input('Enter password: ')
    if username == user and password == pas :
        print('Login successful')
        break
    else :
        c = c - 1 
        print('Wrong username or password')
        print('Attempts remaining:', c)
if c == 0:
    print('Maximum login attempts exceeded')