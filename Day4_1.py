basket_list=[]
choice=0
while(choice!=4):
    print("1. Add Data")
    print("2. View Date")
    print("3. Calculate bill")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        n=int(input("How many items to add: "))
        for i in range(n):
            item_name=input("Enter item to purchase:")
            item_price=int(input("Enter the price of "+item_name+":"))
            item_quantity=int(input("Enter quantity of "+item_name+" to basket"))
            sublist=[item_name,item_price,item_quantity]
            basket_list.append(sublist)
    elif(choice==2):
        n=len(basket_list)
        print("Item_name\tPrice\tQty\tSubtotal")
        for i in range(n):
             print(basket_list[i][0],"\t",basket_list[i][1],"\t",basket_list[i][2],"\t",(basket_list[i][1]*basket_list[i][2]))
    elif(choice==3):
        total_bill=0
        for i in range(len(basket_list)):
            subtotal=basket_list[i][1]*basket_list[i][2]
            total_bill=total_bill+subtotal
        print("Total bill is",total_bill)
    elif(choice==4):
        print("Thankyou!")
        break
    else:
        print("Invalid input")