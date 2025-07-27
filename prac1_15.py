'''
@@@@*       time=1,i=0,space=4,stars=1
@@@**       time=2,i=1,space=3,stars=2
@@*#*       time=3,i=2,space=2,stars=2
@*##*       time=4,i=3,space=1,stars=2
*###*       time=5,i=4,space=0,stars=2
@*##*       time=6,i=0,space=1,stars=2
@@*#*       time=7,i=1,space=2,stars=2
@@@**       time=8,i=2,space=3,stars=2
@@@@*       time=9,i=3,space=4,stars=1

up_space=n-i-1
up_stars=i+1
down_space=i+1
down_stars=n-i-1
'''
n=int(input("How many numbers "))
for i in range(n):
    up_space=n-i-1
    for j in range(up_space):
        print(" ",end="")
    up_stars=i+1
    for k in range(up_stars):
        if(k==0 or k==up_stars-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1):
    down_space=i+1
    for j in range(down_space):
        print(" ",end="")
    down_stars=n-i-1
    for k in range(down_stars):
        if(k==0 or k==down_stars-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()