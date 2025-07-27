from Day_8_Student_class import Student
choice=0
students=[]
while(choice!=3):
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")
    f=open("Choice2.txt","w")
    operation_completed=False
    while(operation_completed==False):
        try:
            choice=int(input("Enter the choice "))
            operation_completed=True
        except Exception as e:
            Choice2=Choice2+str(e)+"\n"
            print("ValueError: invalid literal for int() with base 10: ")
    if(choice==1):
        n=int(input("How many students to add "))
        for i in range(n):
            s=Student()
            s.addStudentDate()
            students.append(s)
    elif(choice==2):
        for i in range(len(students)):
            s=students[i]
            s.viewStudentData()
    elif(choice==3):
        print("thankyou")
    else:
        print("Invalid input")
