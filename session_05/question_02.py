a = input('Please enter str : ')
l = []

for i in a :
    if i not in l : 
        l.append(i)
s = ''.join(l)
print(s)