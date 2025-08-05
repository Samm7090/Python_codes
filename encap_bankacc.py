class bank_acc():
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount

    def deposite(self,amount):
        self.amount += amount
        print(f"{amount} Amount deposted and your total balance is {self.amount}")

    def withdraw(self,amount):
        if amount < self.amount:
            self.amount = self.amount - amount 

        print(f"{amount} is credited to your bank account and your remaining balance is {self.amount}")