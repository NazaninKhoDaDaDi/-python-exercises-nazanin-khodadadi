file = ('C://Users//ASUS//Desktop// python-exercises-nazanin-khodadadi//session_08//txt//transactions.txt')

def total_deposits():
    total = 0
    with open(file , 'r') as add1 :
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')
            
            if parts[1] == 'deposit':
                parts[2] = int(parts[2])
                total = total + parts[2]
        return total
                
def total_withdrawals():
    total = 0
    balances = {}
    with open(file , 'r') as add1 :
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')
            
            username = parts[0]
            transaction = parts[1]
            amount = int(parts[2])
            
            if username not in balances:
                balances[username] = 0
            
            if transaction == 'deposit':
                balances[username] = balances[username] + amount
                
            elif transaction == 'withdraw':
                if amount <= balances[username]:
                   total = total + amount
                   balances[username] = balances[username] - amount
    return total
                

def calculate_balance(username):
    balance = 0

    with open(file, 'r') as add1:
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')

            if parts[0] == username:
                if parts[1] == 'deposit' :
                    balance = balance + int(parts[2])
                elif parts[1] == 'withdraw':
                    if balance >= int(parts[2]):
                       balance = balance - int(parts[2])
    return balance

def find_invalid_transactions():
    balances = {}
    invalid = []
    with open(file , 'r') as add1 :
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')
            
            username = parts[0]
            transaction = parts[1]
            amount = int(parts[2])
            
            if username not in balances:
                balances[username] = 0
            
            if transaction == 'deposit' :
                balances[username] = balances[username] + amount
            elif transaction == 'withdraw' :
                if amount > balances[username]:
                    invalid.append(parts1)
                else:
                    balances[username] = balances[username] - amount
        return invalid
    
def generate_report():
    users = set()

    with open(file, 'r') as add1:
        for i in add1:
            parts1 = i.strip()
            parts = parts1.split(',')
            users.add(parts[0])

    for username in users:
        print('User:', username)
        deposits = 0
        withdrawals = 0
        balance = 0
        with open(file, 'r') as add2:
            for i in add2:
                parts1 = i.strip()
                parts = parts1.split(',')

                if parts[0] == username:
                    amount = int(parts[2])
                    if parts[1] == 'deposit':
                            deposits = deposits + amount
                            balance = balance + amount
                    elif parts[1] == 'withdraw':
                         if amount <= balance:
                            withdrawals = withdrawals + amount
                            balance = balance - amount
                                     
        print('Total deposits:', deposits)
        print('Total withdrawals:', withdrawals)
        print('Balance:', balance)
        
        invalid = find_invalid_transactions()
        for transaction in invalid:
            parts = transaction.split(',')
            if parts[0] == username :
                print('Invalid transaction:', transaction)
print('Total deposits:', total_deposits())
print('Total withdrawals:', total_withdrawals())
print('Ali balance:', calculate_balance('Ali'))
print('Sara balance:', calculate_balance('Sara'))
print()
generate_report()