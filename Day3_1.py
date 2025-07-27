choice=0
grocery_list=[]
while(choice!=5):
    print("1. Add Itmes")
    print("2. Remove Itme")
    print("3. Insert Itme")
    print("4. View Itme")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        n=int(input("Enter how many items to add:"))
        for i in range(n):
            item = input("which item to add:")
            grocery_list.append(item)
        print(n ,"Items added successfully")
    elif(choice == 2):
        item = input("Enter how many item to remove:")
        if(item in grocery_list):
            grocery_list.append(item)
            print(item, "Items removed successfully")
        else:
            print("There is no", item ,"found in list!")
    elif(choice == 3):
        position=int(input("Which position you want to insert"))
        item = input("Which item to insert:")
        grocery_list.insert(position,item)
        print(item,"inserted sucessfully at position", position)
    elif(choice == 4):
        n= len(grocery_list)
        for i in range(n):
            print("item is:",grocery_list[i])
    elif(choice == 5):
        print("you have selected to Exit, Thank you:")
    else:
        print("Invalid choice , try again!")