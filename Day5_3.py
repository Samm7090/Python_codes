grocery_items={}
choice=0
while(choice!=6):
    print("1. Add item")
    print("2. View item")
    print("3. Update item")
    print("4. Remove item")
    print("5. Calculate bill")
    print("6. Exit")
    choice=int(input("Enter your choice"))

    if(choice==1):
        n=int(input("how many items to add"))
        for i in range(n):
            item_name=input("Enter item to add:")
            item_price=int(input("Enter the price: "))
            item_quantity=int(input("Enter the quantity: "))
            sub_item={"price":item_price, "quantity":item_quantity}
            grocery_items[item_name]=sub_item
    elif(choice==2):
        for item in grocery_items:
            print(item,'\t',grocery_items[item]["price"],'\t',grocery_items[item]['quantity'])
    elif(choice==3):
        item_name=input("Enter the product to update: ")
        if(item_name in grocery_items):
            item_key_to_update = input("enter what need to update price/quantity ")
            if(item_key_to_update=="price" or item_key_to_update=="quantity"):
                value_to_update=int(input("Enter the value of"+item_key_to_update))
                grocery_items[item_name][item_key_to_update]
            else:
                print("Invalid properties to update")
        else:
            print(item_name,"not present in items")
    elif(choice==4):
        item_name=input("Enter item to be removed: ")
        if(item_name in grocery_items):
            del grocery_items[item_name]
        else:
            print(item_name,"does not exist!")
    elif(choice==5):
        total_bill=0
        for name,properties in grocery_items.items():
            total_bill=total_bill+(properties["price"]*properties["quantity"])
        print("total bil is ",total_bill)
    elif(choice==6):
        print("Thankyou")
    else:
        print("Invalid ")