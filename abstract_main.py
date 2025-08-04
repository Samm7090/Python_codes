from abstract_credit_payment import credit_card

def make_payment(payment_method,amount):
    payment_method.pay(amount)

if __name__=="__main__":
    cc=credit_card()

    make_payment(cc,2000)