name=input("Enter the name ")
age=int(input("Enter your age "))
gender= input("Enter your gender Male/Female ")
if(gender=="male"):
    if(age<21):
        print("hey", name , "You area not eligible for Matrimony match")
    else:
        print("Yay! Congrats ", name ,"You are eliginle")
elif(gender=="female"):
    if (age < 18):
        print("hey" , name, "You area not eligible for Matrimony match")
    else:
        print("Yay! Congrats ", name, "You are eliginle")
else:
    print("Sorry!inapproprate gender ")