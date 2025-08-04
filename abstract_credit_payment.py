from abstract_payment_interface import payment_interface

class credit_card(payment_interface):
    def pay(self,amount):
        print(f"Paind {amount} using credit card ")