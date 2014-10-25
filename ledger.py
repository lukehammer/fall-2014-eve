class Transaction():
    def __init__(self, amount, payee, memo):
        self.amount = amount
        self.payee = payee
        self.memo = memo

class Account():
    def __init__(self, name , balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction)
        self.balance += transaction.amount

    def printLedger(self):
        print("Ledger...")
        for t in self.transactions:
            print("\t" +" "+ str(t.amount) +" " + t.payee +" "+ t.memo)

account = Account("checking",0)
account.addTransaction(Transaction(3000, "Landlord", "December Rent"))
account.addTransaction(Transaction(3,"Starbucks","Coffee"))
account.printLedger()
savings_account = Account("savings", 9999)
savings_account.addTransaction(Transaction(1000,"Transfer","To_Checking"))

