def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient Funds")
    else:
        balance = (balance - amount)
        print(balance)