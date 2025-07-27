name=input("Enter the name ")
gender= input("Enter your gender Male/Female ")
age=int(input("Enter your age "))
age_criteria=0
if(gender=="male"):
    age_criteria=21
elif(gender=="female"):
    age_criteria=18
if(age >= age_criteria and age_criteria>0):
    print("Hey! Congrates ",name, "You are eligible ")
else:
    print("Sorry! you are not eligible ")