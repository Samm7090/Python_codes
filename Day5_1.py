grocery_list=[["rice",10,20],["wheat",20,50]]
grocery_item={"rice":[10,20],"wheat":[50,10]}
item_search=input("Enter which item to check: ")
if(item_search in grocery_item):
    print("Element found")
else:
    print("Element not found")