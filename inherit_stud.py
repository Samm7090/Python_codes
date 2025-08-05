from Inherit_person import person

class student(person):

    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks=marks

    def show_student_info(self):
        self.show_info()
        print(f"Marks is {self.marks}")


if __name__== "__main__":
    
    s1=student("Sam",24,98)

    s1.show_student_info()
