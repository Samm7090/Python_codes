'''
*****       time=1, i=0,stars=5
*@@*        time=2, i=1,stars=2
*@*         time=3, i=2,stars=2
**          time=4, i=3,stars=2
*           time=5, i=4,stars=1
**          time=6, i=0,stars=2
*@*         time=7, i=1,stars=2
*@@*        time=8, i=2,stars=2
*****       time=9, i=3,stars=5
up_stars=n-i
down_stars=i+2
'''
n=int(input("How many numbers "))
for i in range(n):
    up_stars=n-i
    for j in range(up_stars):
        if(j==0 or j==up_stars-1 or i==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1):
    down_stars=i+2
    for j in range(down_stars):
        if (j == 0 or j == down_stars - 1 or i== n-2 ):
            print("*", end="")
        else:
            print(" ", end="")
    print()