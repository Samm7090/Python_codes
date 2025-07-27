'''
@@@@*           time=1,i=0,space=4,stars=1
@@@*#*          time=2,i=1,space=3,stars=3
@@*###*         time=3,i=2,space=2,stars=5
@*#####*        time=4,i=3,space=1,stars=7
*********       time=5,i=4,space=0,stars=9

space=n-i-1
stars=(2*i)+1
'''
n=int(input("How many numbers "))
for i in range(n):
    num_of_space=n-i-1
    for j in range(num_of_space):
        print(" ",end="")
    num_of_stars=(2*i)+1
    for k in range(num_of_stars):
        if(k==0 or k==num_of_stars-1 or i==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()