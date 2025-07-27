student={}
percentage_list = {}
choice=0
while(choice!=6):
    print("1.Add data")
    print("2.View data")
    print("3.% of student")
    print("4.Higest marks in class")
    print("5.Lowest marks in class")
    print("6.Exit")
    choice=int(input("Enter your choice "))

    if(choice==1):
        n=int(input("How many students to add "))
        for i in range(n):
            student_name=input("Enter student name ")
            student_class=input("Enter class of student ")
            student_div=input("Enter division of student ")

            mark_list=[]
            m=int(input("how many marks of subject do you want to enter "))
            for j in range(m):
                student_marks = int(input("Enter the marks of "+str(j+1)+" Student "))
                mark_list.append(student_marks)

            sub_list=[student_class,student_div,mark_list]
            student[student_name]=sub_list
    elif(choice==2):
        print(student)
    elif(choice==3):

        for student_name in student:
            percentage=int((sum(student[student_name][2])/500)*100)
            percentage_list[student_name]=percentage

            print(student_name,"% of student is",percentage)
    elif(choice==4):
        for student_name in student:
            max_percentage=0

            if(percentage_list[student_name][i]>max_percentage):
                max_percentage=percentage_list[student_name][i]
                print(max_percentage)
