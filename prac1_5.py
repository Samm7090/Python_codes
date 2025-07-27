'''
@@@@*       time=1, i=0,up_space=4, stars=1
@@@***      time=2, i=1,up_space=3, stars=3
@@*****     time=3, i=2,up_space=2, stars=5
@*******    time=4, i=3,up_space=1, stars=7
*********   time=5, i=4,up_space=0, stars=9
@*******    time=2, i=0,down_space=1, stars=7
@@*****     time=3, i=1,down_space=2, stars=5
@@@***      time=4, i=2,down_space=3, stars=3
@@@@*       time=5, i=3,down_space=4, stars=1

up_space=n-i-1
up_stars=(2*i)+1
down_space=i+1
down_star=2*(n-i)-1
'''
n=int(input("How many numbers "))
for i in range(n-1):
    up_space=n-i-1
    for j in range(up_space):
        print(" ",end="")
    up_stars=(2*i)+1
    for k in range(up_stars):
        print("*",end="")
    print()
for i  in range(n):
    down_space = (i+1)-1
    for j in range(down_space):
        print(" ", end="")
    down_stars = 2*(n-i)-1
    for k in range(down_stars):
        print("*", end="")
    print()