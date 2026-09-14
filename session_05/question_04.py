s = input('Enter a sentence : ')
a = s.split(' ')
maximum = 0
word = ''
b = {}

for i in a : 
    if i in b : 
        b[i] = b[i] + 1
    else:
        b[i] = 1
        
for i in b :
    if b[i] > maximum:
        word = i
        maximum = b[i]

print(word , '->' , maximum)