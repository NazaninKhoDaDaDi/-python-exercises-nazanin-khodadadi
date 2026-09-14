s = input('Enter a text: ')

char = ''
count = 0
result = ''

for i in s:
    if i == char:
        count = count + 1

    else:
        if char != '':
            result = result + char + str(count)

        char = i
        count = 1

if char != '':
    result = result + char + str(count)

print(result)