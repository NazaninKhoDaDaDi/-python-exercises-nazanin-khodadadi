s = input('Enter a sentence: ')
maximum = 0
word = ''

a = s.split(' ')

for i in a : 
    if len(i) > maximum : 
        word = i
        maximum = len(i)
        
print(word)
print('Length : ', maximum)
