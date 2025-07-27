text_heading='productid, productname,productprice,prodeuctqty'
text_content=''
n=int(input("how many products to add:"))
for i in range(n):
    item_name=input("Enter product name ")
    item_price=input("Enter product price ")
    item_quantity=input("Enter product quantity ")
    if(item_name not in text_content):
        line_data=str(i+1)+','+item_name+','+item_price+','+item_quantity
        if(i<n-1):
            text_content=text_content+line_data+'\n'
        else:
            text_content = text_content + line_data

data=text_heading+"\n"+text_content
f= open("stock.txt","w")
f.write(data)
f.close()
