employees = {
    'E01': {
        'name': 'Ali',
        'age': 28,
        'salary': 3000
    },
    'E02': {
        'name': 'Sara',
        'age': 32,
        'salary': 4500
    },
    'E03': {
        'name': 'Reza',
        'age': 25,
        'salary': 2800
    }
}

maximum = 0
maximum_name = ''
minimum = 999999
minimum_name = ''
total = 0

for i in employees:
    if employees[i]['salary'] > maximum :
        maximum = employees[i]['salary']
        maximum_name = employees[i]['name']
print('Employee : ', maximum_name)
print('Maximum Salary : ',maximum)
print()

for i in employees:
    total = total + employees[i]['salary']
average = round(total / len(employees), 2)
print('Average :', average)
print()

for i in employees:
    if employees[i]['salary'] > 3000:
        print('Salary > 3000 :',employees[i]['name'])
print()

for i in employees:
    if employees[i]['salary'] < minimum :
        minimum = employees[i]['salary']
        minimum_name = employees[i]['name']
print('Employee : ', minimum_name)
print('Minimum Salary : ', minimum)
