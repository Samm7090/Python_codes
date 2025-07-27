'''
*********       time=1,i=0,space=0,stars=9
@*#####*        time=2,i=1,space=1,stars=2
@@*###*         time=3,i=2,space=2,stars=2
@@@*#*          time=4,i=3,space=3,stars=2
@@@@*           time=5,i=4,space=4,stars=1
@@@*#*          time=6,i=0,space=3,stars=2
@@*###*         time=7,i=1,space=2,stars=2
@*#####*        time=8,i=2,space=1,stars=2
*********       time=9,i=3,space=0,stars=9

up_space=i
up_stars=2*(n-i)-1
down_space=n-i-2
down_stars=(n-2)+(2*i)
'''
n=int(input("How many numbers "))
for i in range(n):
    up_space=i
    for j in range(up_space):
        print(" ",end="")
    up_stars=2*(n-i)-1
    for k in range(up_stars):
        if(k==0 or k==up_stars-1 or i==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1):
    down_space=n-i-2
    for j in range(down_space):
        print(" ",end="")
    down_stars=(n-2)+(2*i)
    for k in range(down_stars):
        if(k==0 or k==down_stars-1 or i==n-2):
            print("*",end="")
        else:
            print(" ",end="")
    print()