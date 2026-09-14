a = input('Enter Sentence 1:')
b = input('Enter Sentence 2:')
found = False

c = a.split()
d = b.split()

print('Common words:')

for i in c:
    if i in d :
        print(i)
        found = True


if found == False:
    print('No common words found')