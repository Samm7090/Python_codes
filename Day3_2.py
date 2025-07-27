name_list=[]
marks_list=[]
choice=0
while(choice!=5):
    print("1. Add Data")
    print("2. View Date")
    print("3. View Lowest marks Data")
    print("4. View Highest marks Data")
    print("5. Exit")
    choice=int(input("How many students data to add"))
    if(choice==1):
        n= int(input("How many students data to add"))
        for i in range(n):
            name = input("Enter student name")
            marks = int(input("Enter marks of student"))
            name_list.append(name)
            marks_list.append(marks)
        print(n, "Students data added successfully!")
    elif(choice==2):
        n = len(name_list)
        for i in range(n):
            print("Student ",name_list[i],"has scored",marks_list[i],"marks")

    elif(choice==3):
        if(len(marks_list)>0):
            lowestmarks = min(marks_list)
            position = marks_list.index(lowestmarks)
            print("Lowest marks", lowestmarks ,"scored by", name_list[position])
        else:
            print("no data found")

    elif(choice == 4):
        if (len(marks_list) > 0):
            highestmarks = max(marks_list)
            position = marks_list.index(highestmarks)
            print("Highest marks", highestmarks, "scored by", name_list[position])
        else:
            print("no data found")
    elif(choice == 5):
        print("thank you! ")
    else:
        print("Invalid input")
