def get_values():
    values = []
    count = int(input('How many values? '))

    for i in range(0, count):
        value = input('Enter a value: ')
        values.append(value)

    return values


def add_unique(value, unique_values):
    if value == '':
        print('Empty value is not allowed!')
        return False, None

    for i in range(len(unique_values)):
        if value.lower() == unique_values[i].lower():
            return False, i + 1

    unique_values.append(value)
    return True, None


def process_values(values):
    unique_values = []
    duplicate_count = 0
    first_positions = []

    position = 0

    for i in values:
        position = position + 1

        if i == '':
            print('Empty value is not allowed!')
            continue

        result, duplicate_position = add_unique(i, unique_values)

        if result == False:
            duplicate_count = duplicate_count + 1
            print('Duplicate value, first entered at position', duplicate_position ,'→', i)

        elif result == True:
            print('New value added to the list →', i)
            first_positions.append(position)

    unique_count = len(unique_values)

    return unique_values, unique_count, duplicate_count, first_positions

def show_report(values):
    unique_values, unique_count, duplicate_count, first_positions = process_values(values)
    

    print('Unique values:', unique_values)
    print('Number of duplicate values:', duplicate_count)
    print('Number of unique values:', unique_count)
    
    print('First positions:')

    for i in range(len(unique_values)):
        print(unique_values[i], '→', first_positions[i])
    
    
    
values = get_values()
show_report(values)