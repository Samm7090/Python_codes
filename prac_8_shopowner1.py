from prac_8_shopowner import Stock

choice=0
stock_list=[]
while(choice!=3):
    print("1.Add Stock ")
    print("2.View Stock ")
    print("3. Exit")
    f1 = open("Choice2.txt", "w")
    str_choice=""
    operation_completed = False
    while (operation_completed == False):
        try:
            choice = int(input("Enter the choice "))
            operation_completed = True
        except Exception as e:
            str_choice = str_choice + str(e) + "\n"
            print("ValueError: invalid literal for int() with base 10: ")
    f1.write(str_choice)
    f1.close()


    if(choice==1):

        s=Stock()
        s.addStock()
        stock_list.append(s)

    elif(choice==2):
        for i in range(len(stock_list)):
            s=stock_list[i]
            s.veiwStock()

    elif(choice==3):
        print("Thankyou! ")

    else:
        print("Invalid input ")