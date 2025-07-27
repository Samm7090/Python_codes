'''
*********       time=1,i=0,space=0,stars=9
@*#####*        time=2,i=1,space=1,stars=7
@@*###*         time=3,i=2,space=2,stars=5
@@@*#*          time=4,i=3,space=3,stars=3
@@@@*           time=5,i=4,space=4,stars=1

space=i
stars=2*(n-i)-1
'''
n=int(input("How many numbers "))
for i in range(n):
    num_of_space=i
    for j in range(num_of_space):
        print(" ",end="")
    num_of_stars=2*(n-i)-1
    for k in range(num_of_stars):
        if(k==0 or k==num_of_stars-1 or i==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()