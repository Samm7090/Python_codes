class bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposite(self):
        amount=int(input("Enter amount to deposite: "))
        self.balance= self.balance+amount
    
    def withdraw(self):
        amount=int(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount

    def check_balance(self):
        return self.balance
    

