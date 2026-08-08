a = 0
for i in range(1,11):
    if i % 2 == 1 :
        a = a +  i * 5
    elif i % 2 == 0:
        a = a + i + 5
print('Toltal : ' , a)