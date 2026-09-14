s = input('Enter a text: ')

words = ['hack', 'fraud', 'scam', 'password', 'atack']
found = False

a = s.split(' ')

for i in words:
    if i in a : 
        found = True
        c = a.count(i)
        print(i , '->' , c)
        
if found == False : 
    print('No matching words found')