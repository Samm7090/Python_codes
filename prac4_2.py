stock_list=[["rice",50,100,],["wheat",30,200]]
grocery_list=[]
choice=0
while(choice!=5):
    print("1.View stock")
    print("2.Add basket")
    print("3.View basket")
    print("4.Calculate bill")
    print("5.Exit")
    choice=int(input("Enter your choice "))

    if(choice==1):
      print(stock_list)

    elif(choice==2):
        n=int(input("How many items to add in basket "))
        for i in range(n):
            if(len(grocery_list)==i):
                item_name = input("Enter item you want ")
                if(item_name=="rice" or item_name=="wheat"):
                    item_quantity=int(input("Enter the quantity "))
                    sublist=[item_name,item_quantity]
                    grocery_list.append(sublist)

                    stock_list[i][2]=stock_list[i][2]-grocery_list[i][1]

                else:
                    print(item_name+" is outof stock")

            else:
                item_quantity1=0
                for i in range(n):
                    item_name = input("Enter item you want ")
                    if (item_name == "rice" or item_name == "wheat"):
                        item_quantity1=int(input("Enter the quantity "))
                        item_quantity=item_quantity + item_quantity1
                        if(item_name=="rice"):
                            grocery_list[0][1]=item_quantity
                        else:
                            grocery_list[0][2]=item_quantity

                        stock_list[i][2] = stock_list[i][2] - item_quantity1

    elif(choice==3):
        print(grocery_list)

    elif(choice==4):
        total_bill=[]
        sum = 0
        for i in range(len(grocery_list)):
            total_item_bill=stock_list[i][1]*grocery_list[i][1]
            total_bill.append(total_item_bill)
            print(grocery_list[i][0]," is ",total_bill[i],"Rs")
        for j in range(len(total_bill)):
            sum=sum+total_bill[j]
        print("**************************")
        print("Your Total bill is ",sum)
        print("Thankyou! ")

    elif(choice==5):
        print("Thankyou! Visit again ")
        break

    else:
        print("Invalid input! ")
