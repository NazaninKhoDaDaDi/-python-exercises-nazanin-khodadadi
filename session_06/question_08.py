users = [
    ("Ali", 25, "Python"),
    ("Sara", 30, "Java"),
    ("Reza", 22, "Python"),
    ("Mina", 28, "C++"),
    ("John", 35, "Python"),
    ("David", 30, "Java")
]
language_users = {}
language_ages = {}
maximum1 = 0
maximum_language = ''
     
for i in users:
    if i[2] in language_users:
        language_users[i[2]].append(i[0])
    else:
        language_users[i[2]] = [i[0]]
print(language_users)
print()

for i in users:
    if i[2] in language_ages:
        language_ages[i[2]].append(i[1])
    else:
        language_ages[i[2]] = [i[1]]
        
for i in language_ages:
   average = sum(language_ages[i]) / len(language_ages[i])
   print(i, '->', average)
print()
   
for i in language_ages:
    maximum = max(language_ages[i])
    
    for j in users:
            if j[2]==i and j[1]==maximum:
                print('Oldest user in', i, '->', j[0])
print()

for i in language_users:
    if len(language_users[i]) > maximum1:
        maximum1 = len(language_users[i])
        maximum_language = i
print('Language with most users:', maximum_language)
print()

print('Programming languages:')
for i in language_users:
    print(i)
    