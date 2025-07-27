def print_full_name(first, last):
    # Write your code here
    if len(first) and len(last) <= 10:
        print("Hello",first,last+"!","You just delved into python.")
    
if __name__ == '__main__':
    first_name = input("Enter Firstname: ")
    last_name = input("Enter Lastname: ")
    print_full_name(first_name, last_name)