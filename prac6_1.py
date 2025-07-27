name=input("Enter the name you want ")
choice=0
while(choice!=6):
    print("1. Split the name ")
    print("2. 3 Initials of first name and last name ")
    print("3. Reverse the Entire string ")
    print("4. Reverse first name ")
    print("5. Reverse second name ")
    print("6. Exit ")
    choice=int(input("Enter your choice "))

    if(choice==1):
        split_name=name.split(" ")
        print("The name which is splited by space is ",split_name)

    elif(choice==2):
        split_name = name.split(" ")
        for i in range(len(split_name)):
            if(split_name[i]):
                print(split_name[i][0:3])

    elif(choice==3):
        print(name[::-1])

    elif(choice==4):
        name1 = name.split(" ")
        frist_name=name1[0]
        print(name[len(frist_name)-1::-1])

    elif(choice==5):
        name1=" "
        for i in range(len(name1)):
            if(i>0):
                name1 = name.split(" ")
                frist_name = name1[0]
                print(name[len(name):len(frist_name) - 1:-1])
            else:
                print(name[::-1])