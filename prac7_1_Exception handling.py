choice=0

while(choice!=4):
    print("1.Write data ")
    print("2.read data ")
    print("3. Calculate data ")
    print("4.Exit")

    choice=int(input("Enter your choice "))
    text_heading = 'productid, productname,productprice,prodeuctqty'
    text_content = ''
    if(choice==1):
        f=open("choice1_user.txt","w")
        choice1_user=''
        operation_completed=False
        while(operation_completed==False):
            try:
                n = int(input("how many products to add:"))
                for i in range(n):
                    item_name = input("Enter product name ")
                    try:
                        item_price = int(input("Enter product price "))
                        item_quantity = int(input("Enter product quantity "))
                        operation_completed=True
                    except Exception as e:
                        choice1_user=choice1_user+str(e)+'\n'
                        print("Please enter integer value")
                    if (item_name not in text_content):
                        line_data = str(i + 1) + ',' + item_name + ',' + item_price + ',' + item_quantity
                        if (i < n - 1):
                            text_content = text_content + line_data + '\n'
                        else:
                            text_content = text_content + line_data
                operation_completed=True
            except Exception as e:
                choice1_user=choice1_user+str(e)+'\n'
                print("Please enter valid input ")
        f.write(choice1_user)
        f.close()
        data = text_heading + "\n" + text_content
        f = open("stock.txt", "w")
        f.write(data)
        f.close()
    elif(choice==2):
        f = open("stock.txt","r")
        data=f.read()
        f.close()

        file_data_lines=data.split("\n")
        text_heading=file_data_lines[0].split(',')
        print(text_heading[0],'\t',text_heading[1],'\t',text_heading[2],'\t',text_heading[3])
        for i in range(1,len(file_data_lines)):
            line_data=file_data_lines[i]
            product_data=line_data.split(',')
            print(int(product_data[0]), '\t', product_data[1], '\t', int(product_data[2]), '\t', int(product_data[3]))

    elif(choice==3):
        f = open("stock.txt","r")
        data=f.read()
        f.close()

        file_data_lines=data.split("\n")
        total_bill=0
        for i in range(1,len(file_data_lines)):
            line_data=file_data_lines[i]
            product_data=line_data.split(',')
            total_bill=total_bill+(int(product_data[2])*int(product_data[3]))
        print("Your total bill is ",total_bill)