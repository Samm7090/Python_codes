grocery_list=[]
rate_list=[]
quantity_list=[]
Total_list=[]
choice=0
while(choice!=5):
    print("1. Add Data")
    print("2. View Date")
    print("3. Calculate bill")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        n=int(input("Enter how many items to add in list: "))
        for i in range(n):
            item= input("Enter which item to add: ")
            rate= int(input("Enter the rate for per KG: "))
            quantity= int(input("Enter quantity in KG: "))
            grocery_list.append(item)
            rate_list.append(rate)
            quantity_list.append(quantity)
        print(n,"Item added successfully")
    elif(choice==2):
        n = len(grocery_list)
        for i in range(n):
            print(grocery_list[i],"is",rate_list[i],"rs KG and quantity is",quantity_list[i],"KG")
    elif(choice==3):
        n= len(rate_list)
        for i in range(n):
            Total = (rate_list[i] * quantity_list[i])
            Total_list.append(Total)
            print(grocery_list[i], Total_list[i])
        sum=0
        for i in range(n):
            sum=sum+Total_list[i]
        print("Total bill ",sum)
    elif(choice==4):
        print("Thankyou!")
        break
    else:
        print("Invalid input")