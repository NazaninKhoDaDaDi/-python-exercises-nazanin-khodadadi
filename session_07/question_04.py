transactions = [
    ('Ali', 'deposit', 50000000, 10),
    ('Ali', 'withdraw', 2000000, 11),
    ('Ali', 'withdraw', 3000000, 12),
    ('Ali', 'withdraw', 4000000, 13),
    ('Ali', 'withdraw', 5000000, 14),
    ('Ali', 'withdraw', 6000000, 15),
    ('Sara', 'deposit', 50000000, 20),
    ('Sara', 'withdraw', 60000000, 21),
    ('Reza', 'deposit', 150000000, 30)
]


def check_large_transaction(transaction):
    if transaction[2] > 100000000:
        return True
    return False


def check_repeated_withdrawals(transactions):
    count = 0
    suspicious = []

    for i in transactions:
        if i[1] == 'withdraw':
            count = count + 1

            if count > 3:
                suspicious.append(i)
        else:
            count = 0

    return suspicious


def check_balance(transaction, balance):
    if transaction[1] == 'withdraw' and transaction[2] > balance:
        return True
    return False


def generate_fraud_report(transactions):
    report = []
    balances = {}
    repeated = check_repeated_withdrawals(transactions)

    for i in transactions:
        user = i[0]
        balance = balances.get(user, 0)

        if check_large_transaction(i) or check_balance(i, balance):
            if i not in report:
                report.append(i)

        if i[1] == 'deposit':
            balances[user] = balance + i[2]

        if i[1] == 'withdraw':
            balances[user] = balance - i[2]

    for i in repeated:
        if i not in report:
            report.append(i)

    return report


def detect_fraud(transactions):
    return generate_fraud_report(transactions)


print(detect_fraud(transactions))
