class Student:
    studName=""
    studClass=""
    studDiv=""
    studMarks={"sub1":0,"sub2":0,"sub3":0,"sub4":0,"sub5":0}

    def addStudentDate(self):
        self.studName=input("Enter Student Name: ")
        self.studClass = input("Enter Student Class: ")
        self.studDiv = input("Enter Student Div: ")
        for i in range(5):
            sub_name="sub"+str(i+1)
            sub_marks=int(input("Enter the marks for "+sub_name))
            self.studMarks[sub_name]=sub_marks
    def viewStudentData(self):
        print("Student Name:",self.studName)
        print("Student Class:", self.studClass)
        print("Student Division:", self.studDiv)
        print("Student Marks:", self.studMarks)