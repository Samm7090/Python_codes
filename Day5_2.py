grocery_items={}
n=int(input("How many items to add "))
for i in range(n):
    item_name=input("Enter the name of item ")
    item_price=int(input("Enter the price of the item "))
    grocery_items[item_name]=item_price
print(grocery_items)

item_name_to_update=input("Enter name to update ")
item_price_to_update=int(input("Enter updates price"))
if(item_name_to_update in grocery_items):
    grocery_items[item_name_to_update]=item_price
else:
    print(item_name_to_update,"not in grocery ")
print(grocery_items)


item_name_to_remove=input("Enter name to remove ")
if(item_name_to_remove in grocery_items):
    del grocery_items[item_name_to_remove]
else:
    print(item_name_to_remove,"not in grocery")
for item in grocery_items:
    print(item,grocery_items[item])
for pair in grocery_items:
    print(pair[0],pair[1])
for name,price in grocery_items.items():
    print(name,price)

