import threading
import datetime

class account:
    def __init__(self, id, balance, widthdraw_limit=-1, transfer_limit=-1):
        self.id, self.balance, self.widthdraw_limit, self.transfer_limit \
            = id, balance, widthdraw_limit, transfer_limit
        self.lock = threading.Lock()
        self.transaction_history = []

    def setWidthdrawLimit(self, limit:int):
        if limit < -1:
            raise Exception(f"Invalid parameter - limit cannot be less than -1.")
        self.widthdraw_limit = limit

    def setTransferLimit(self, limit:int):
        if limit < -1:
            raise Exception(f"Invalid parameter - limit cannot be less than -1.")
        self.transfer_limit = limit

class transaction:
    def __init__(self, account_id, type, amount:int, time=datetime.datetime.now()):
        self.account_id, self.type, self.amount, self.time = \
            account_id, type, amount, time

    def __str__(self):
        return f"account_id={self.account_id}, type={self.type}, amount={self.amount}, time={self.time}"


class banking:
    def transfer(self, accountFrom:account, accountTo:account, amount:int):
        # validations
        if amount <= 0:
            raise Exception("Invalid money amount, must be more than zero")
        if accountFrom.transfer_limit >= 0 and accountFrom.transfer_limit < amount:
            raise Exception("Money amount is more than account transfer limit")
        if accountFrom.balance < amount:
            raise Exception("Not enough money to tranfer in account")

        # lock for transaction
        with (accountFrom.lock and accountTo.lock):
            accountFrom.balance -= amount
            accountTo.balance += amount
            # record history
            trans1 = transaction(accountFrom.id, "Transfer", amount)
            accountTo.transaction_history.append(trans1)
            trans2 = transaction(accountTo.id, "Transfer", amount)
            accountFrom.transaction_history.append(trans2)

    def deposit(self, accountTo:account, amount:int):
        # validations
        if amount <= 0:
            raise Exception("Invalid money amount, must be more than zero")

        # lock for transaction
        with (accountTo.lock):
            accountTo.balance += amount
            trans = transaction(accountTo.id, "Deposit", amount)
            accountTo.transaction_history.append(trans)
    
    def widthdraw(self, accountFrom:account, amount:int):
        # validations
        if amount <= 0:
            raise Exception("Invalid money amount, must be more than zero")
        if accountFrom.widthdraw_limit >= 0 and accountFrom.widthdraw_limit < amount:
            raise Exception("Money amount is more than account widthdraw limit")
        if accountFrom.balance < amount:
            raise Exception("Not enough money to widthdraw")
        
        # lock for transaction
        with (accountFrom.lock):
            accountFrom.balance -= amount
            trans = transaction(accountFrom.id, "Widthdraw", amount)
            accountFrom.transaction_history.append(trans)

acct1 = account(id="123", balance=100)
acct2 = account(id="456", balance=200)
banking1 = banking()
# test transaction
banking1.transfer(acct1, acct2, 50)
banking1.deposit(acct1, 90)
print(f"balance1={acct1.balance}, balance2={acct2.balance}")
for trans in acct1.transaction_history:
    print(trans)
# test limit
acct1.setWidthdrawLimit(limit=30)
banking1.widthdraw(acct1, 90)