student=[]
percentage_list=[]
choice=0
while(choice!=8):
    print("1. Add Data")
    print("2. View Date")
    print("3. % of student")
    print("4. Highest marks in class")
    print("5. Lowest marks in class")
    print("6. Subject wise topper")
    print("7. Class wise topper")
    print("8. Exit")
    choice=int(input("Enter your choice: "))
    if (choice == 1):
        n = int(input("How many Students to add: "))
        for i in range(n):
            student_name = input("Enter the name :")
            student_class = input("Enter the class of student:")
            student_division = input("Enter division of student:")
            mark_list = []
            subject_list=[]
            for j in range(5):
                subject = input("Enter th subject of stuent" + str(j + 1) + ":")
                marks = int(input("Enter marks of student" + str(j + 1) + ":"))
                mark_list.append(marks)
                subject_list.append(subject)
            sublist = [student_name, student_class, student_division, mark_list,subject_list]
            student.append(sublist)
    elif (choice == 2):
        n = len(student)
        for i in range(n):
            print(student[i][0], student[i][1], student[i][2],"\n",student[i][4][0], student[i][3][0],"\n", student[i][4][1],student[i][3][1],"\n", student[i][4][2],student[i][3][2],"\n",
                  student[i][4][3],student[i][3][3],"\n", student[i][4][4],student[i][3][4])
    elif (choice == 3):
        percentage_list = []
        for i in range(len(student)):
            mark_list = student[i][3]
            percentage = (sum(mark_list) / 500) * 100  # sum(marklist)/len(markslist)
            percentage_list.append(percentage)
            student_name = student[i][0]
            student_class = student[i][1]
            student_division = student[i][2]
            print(student_name, student_class, student_division, percentage)
    elif (choice == 4):
        if (len(percentage_list) > 0):
            higest_percentage = max(percentage_list)
            higest_percentage_index = higest_percentage.index(higest_percentage)
            print(student[higest_percentage_index][0], "has scored higest percentage", higest_percentage, "%")
        else:
            print("please calculate % to get the higest score data")
    elif (choice == 5):
        if (len(percentage_list) > 0):
            lowest_percentage = min(percentage_list)
            lowest_percentage_index = lowest_percentage.index(lowest_percentage)
            print(student[lowest_percentage_index][0], "has scored higest percentage", lowest_percentage, "%")
        else:
            print("please calculate % to get the higest score data")
    elif(choice == 6):
        for i in range(len(mark_list)):
            max_marks=0
            max_stud_index=0

            for j in range(len(student)):
                if(student[j][3][i]>max_marks):
                    max_marks=student[j][3][i]
                    max_stud_index=j
            print(student[j][4][i],"Subject Topper is ",student[max_stud_index][0],"who had scored ",max_marks," marks")

    elif(choice==7):
        max_percent=0
        max_percent_index=0
        for j in range(len(student)):
            if(percentage_list[j]>max_percent):
                max_percent=percentage_list[j]
                max_percent_index=j
        print(student[max_percent_index][0]," is topper of class who has scored ",max_percent,"%")

    elif (choice == 8):
        print("Thankyou")
        break
    else:
        print("Invalid input")