from prac_8_coustomer import Basket

choice=0
basket_list=[]
while(choice!=4):
    print("1.Add Basket")
    print("2.View Basket")
    print("3.Calculate bill")
    print("4.Exit")
    choice=int(input("Enter your choice: "))

    if(choice==1):
        s=Basket()
        s.addBasket()
        basket_list.append(s)

    elif(choice==2):
        for i in range(len(basket_list)):
            s=basket_list[i]
            s.veiwBasket()

    elif(choice==3):
        print(len(basket_list))


