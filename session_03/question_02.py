s = 0
for i in range(1,11):
    n=int(input('Please enter the athletes jump height : '))
    if n > s :
        s = n
        print('The highest jump recorded.')
    elif n == s:
        print('This jump has already been recorded.')
        
print('Your record : ' , s)
