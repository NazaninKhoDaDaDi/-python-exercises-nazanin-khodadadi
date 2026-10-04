s = input('Please enter str: ')
letters = {}

for i in s :
    if i.isalpha():
        if i in letters:
            letters[i] = letters[i] + 1
        else:
            letters[i] = 1
print(letters)
        
    