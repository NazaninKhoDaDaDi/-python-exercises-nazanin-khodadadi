a = input('Please enter string : ')
n = len(a)
if n % 2 == 0:
    print(a[0  : n // 2 ])
elif n % 2 == 1:
    print(a[n // 2 : n])
