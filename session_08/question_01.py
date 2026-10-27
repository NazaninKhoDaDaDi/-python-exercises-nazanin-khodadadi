file = ('C://Users//ASUS//Desktop// python-exercises-nazanin-khodadadi//session_08//txt//users.txt')
def add_user():
    username = input('Enter username:')
    password = input('Enter password:')
    status = 'active'

    with open(file, 'r') as add1:
        found = False

        for i in add1:
            parts = i.strip()
            parts = parts.split(',')

            if parts[0] == username:
                print('Username already exists')
                found = True
                
    if found == False:
        with open(file, 'a') as add2:
            add2.write(username + ',' + password + ',' + status + '\n')
        print('User added successfully')


def find_user():
    username = input('Enter username:')

    with open(file, 'r') as add1:
        found = False

        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')

            if parts[0] == username:
                print(parts1)
                found = True

    if found == False:
        print('User not found')


def delete_user():
    username = input('Enter username:')
    users = []
    found = False

    with open(file, 'r') as add1:
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')

            if parts[0] == username:
                found = True
            else:
                users.append(parts1)

    with open(file, 'w') as add2:
        for i in users:
            add2.write(i + '\n')

    if found:
        print('User deleted successfully')
    else:
        print('User not found')

def generate_report():
    active_count = 0
    blocked_count = 0
    with open(file, 'r') as add2:
        for i in add2:
            parts = i.strip()
            parts = parts.split(',')
            
            if parts[2] == 'active' :
                active_count = active_count + 1
            elif parts[2] == 'blocked' :
                blocked_count = blocked_count + 1
                     
    print('Active users:', active_count)
    print('Blocked users:', blocked_count)
    
while True:
    print('1. Add user')
    print('2. Find user')
    print('3. Delete user')
    print('4. Generate report')
    print('5. Exit')

    a = input('Enter your choice: ')
    
    if a == '1':
        add_user()
        
    
    elif a == '2' :
        find_user()
        
    
    elif a == '3' :
        delete_user()
        
    elif a == '4' :
        generate_report()
        
    elif a == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')