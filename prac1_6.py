'''
*********   time=1, i=0,up_space=0, up_stars=9
@*******    time=2, i=1,up_space=1, up_stars=7
@@*****     time=3, i=2,up_space=2, up_stars=5
@@@***      time=4, i=3,up_space=3, up_stars=3
@@@@*       time=5, i=4,up_space=4, up_stars=1
@@@***      time=6, i=0,down_space=3, down_stars=3
@@*****     time=7, i=1,down_space=2, down_stars=5
@*******    time=8, i=2,down_space=1, down_stars=7
*********   time=9, i=3,down_space=0, down_stars=9
up_space=i
up_stars=2*(n-i)-1
down_space=n-2-i
down_stars=(n-1)+(2*i)
'''
n=int(input("How many numbers "))

for i in range(n):
    up_space = i
    for j in range(up_space):
        print(" ", end="")
    up_star = 2*(n-i)-1
    for k in range(up_star):
        print("*", end="")
    print()
for i in range(n-1):
    down_space = n-2-i
    for j in range(down_space):
        print(" ", end="")
    down_star = (n-2)+(2*i)
    for k in range(down_star):
        print("*", end="")
    print()