file = ('C://Users//ASUS//Desktop// python-exercises-nazanin-khodadadi//session_08//txt//logs.txt')


def count_successful_logins():
    count = 0

    with open(file, 'r') as add1:
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')

            if parts[1] == 'LOGIN' and parts[2] == '200':
                count = count + 1

    return count


def count_failed_logins():
    count = 0

    with open(file, 'r') as add1:
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')

            if parts[1] == 'LOGIN' and parts[2] != '200':
                count = count + 1

    return count

def find_suspicious_users():
    errors = {}
    suspicious_users = []

    with open(file, 'r') as add1:
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')
            if parts[1] == 'LOGIN' and parts[2] == '403':
                  if parts[0] in errors.keys() : 
                        errors[parts[0]] = errors[parts[0]] + 1
                  else :
                        errors[parts[0]] = 1
        for user in errors:
            if errors[user] >= 3 :
                suspicious_users.append(user)
        print('Suspicious users:', suspicious_users)
        
def generate_report():
    print('Successful logins:', count_successful_logins())
    print('Failed logins:', count_failed_logins())
    find_suspicious_users()
    
    operations = {}

    with open(file, 'r') as add1:
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')
            if parts[0] in operations:
                operations[parts[0]] = operations[parts[0]] + 1
            else :
                operations[parts[0]] = 1
    print('Operations per user:', operations)

generate_report()
                    