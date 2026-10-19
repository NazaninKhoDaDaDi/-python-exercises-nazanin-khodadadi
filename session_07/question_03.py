transactions = [
   ('Ali', 'deposit', 5000000),
   ('Ali', 'withdraw', 1000000),
   ('Sara', 'deposit', 8000000),
   ('Ali', 'withdraw', 500000),
   ('Sara', 'withdraw', 2000000),
   ('Reza', 'deposit', 10000000)
]

def analyze_transactions(transactions):
    result = {}
    for i in transactions :
        user = i[0]
        transaction_type  = i[1]
        amount = i[2]
        
        if user not in result :
            result[user] = {
                'deposits': 0,
                'withdrawals': 0,
                'balance_change': 0,
                'transactions': 0 } 
 
        if transaction_type == 'deposit':
            result[user]['deposits'] = result[user]['deposits'] + amount
        elif transaction_type == 'withdraw':
            result[user]['withdrawals'] = result[user]['withdrawals'] + amount
        
        result[user]['transactions'] =  result[user]['transactions'] + 1
        
        result[user]['balance_change'] = result[user]['deposits'] - result[user]['withdrawals']
        
    return result

result = analyze_transactions(transactions)
print(result)

max_deposit = 0
top_depositor = ''

for i in result :
        deposit = result[i]['deposits']
        if deposit > max_deposit :
            max_deposit = deposit
            top_depositor = i
print('Highest deposit:', max_deposit)
print('Top depositor:', top_depositor)

max_withdrawal = 0
top_withdrawer = ''

for i in result:
    withdrawal = result[i]['withdrawals']
    if withdrawal > max_withdrawal:
        max_withdrawal = withdrawal
        top_withdrawer = i
print('Highest withdrawal:', max_withdrawal)
print('Top withdrawer:', top_withdrawer)

max_transactions = 0
most_active_user = ''

for i in result:
    count = result[i]['transactions']
    if count > max_transactions:
        max_transactions = count
        most_active_user = i
print('Most active user:', most_active_user)
print('Number of transactions:', max_transactions)

            