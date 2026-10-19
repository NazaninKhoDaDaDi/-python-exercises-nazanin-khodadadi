logs = [
    ("Ali", "LOGIN", 200),
    ("Ali", "DOWNLOAD", 200),
    ("Sara", "LOGIN", 403),
    ("Reza", "LOGIN", 200),
    ("Sara", "LOGIN", 403),
    ("Sara", "LOGIN", 403)
]

def count_logins(logs):
    successful_logins = 0
    failed_logins = 0

    for i in logs:
        if i[1] == "LOGIN" and i[2] == 200:
            successful_logins = successful_logins + 1
        elif i[1] == "LOGIN" and i[2] == 403:
            failed_logins = failed_logins + 1

    return successful_logins, failed_logins

def check_suspicious_users(logs):
    errors = {}
    suspicious = []
    
    for i in logs:
        user = i[0]
        if i[2] == 403:
            errors[user] = errors.get(user, 0) + 1
            
    for i in errors:
          if errors[i]  >=  3:
               suspicious.append(i)
    return suspicious

def count_operations(logs):
    operations = {}
    
    for i in logs :
        user = i[0]
        operations[user] = operations.get(user, 0) + 1
    return operations

def generate_report(logs):
    logins = count_logins(logs)
    suspicious = check_suspicious_users(logs)
    operations = count_operations(logs)

    report = {
        'logins': logins,
        'suspicious_users': suspicious,
        'operations': operations
    }

    return report
 
print(generate_report(logs))   
            