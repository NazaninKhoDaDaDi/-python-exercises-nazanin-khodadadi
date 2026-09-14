s = input('Enter text: ')

letters = 0
upper = 0
lower = 0
digits = 0
spaces = 0
special = 0

for i in s : 
    if i.isalpha():
        letters = letters + 1
    elif i.isdigit() :
        digits = digits + 1
    
    if i.isupper():
        upper = upper + 1
    elif i.islower() :
        lower = lower + 1
    elif i == ' ':
        spaces = spaces + 1
    elif not i.isdigit() and not i.isalpha() and i != '' : 
        special = special + 1   
        
print('Leters : ' , letters )
print('Uppercase : ' , upper )
print('Lowercase : ' , lower )
print('Digits: ' , digits )
print('Spaces: ' , spaces )
print('Special characters: ' , special )


