students = {
'Ali': [18, 17, 20],
'Sara': [15, 19, 18],
'Reza': [12, 14, 10],
'Mina': [20, 20, 19] }

maximum_average = 0
best_student = ''


for i in students:
    average = round(sum(students[i]) / len(students[i]), 2)
    print(i)
    print('Average:', average)
    print('Highest Grade:', max(students[i]))
    
    if average >= 15:
        print('Status : Passed')
    else:
        print('Status : Failed')

    print()
    
    if average > maximum_average:
        maximum_average = average
        best_student = i
print('Best student:',best_student)
print('Maximum Average :',maximum_average)