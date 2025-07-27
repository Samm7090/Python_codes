try:
    num=int(input("Enter the number:"))
    list_of_numbers=[]
    position=int(input("Which index of list you want "))
    list_of_numbers[position]=num
except IndexError as e:
    print("list position does not exist ")
except ValueError as e:
    print("Value Error ")