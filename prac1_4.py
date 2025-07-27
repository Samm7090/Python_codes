'''
*****   time=1, i=0, up_space=0, stars=5
@****   time=2, i=1, up_space=1, stars=4
@@***   time=3, i=2, up_space=2, stars=3
@@@**   time=4, i=3, up_space=3, stars=2
@@@@*   time=5, i=4, up_space=4, stars=1
@@@**   time=6, i=0, down_space=3, stars=2
@@***   time=7, i=1, down_space=2, stars=3
@****   time=8, i=2, down_space=1, stars=4
*****   time=9, i=3, down_space=0, stars=5

up_space=i
up_stars=n-i
down_space=(n-2)-i
down_stars=n-((n-2)-i)
'''
n=int(input("How many numbers "))

for i in range(n):
    up_space = i
    for j in range(up_space):
        print(" ", end="")
    up_star = n-i
    for k in range(up_star):
        print("*", end="")
    print()
for i in range(n-1):
    down_space = (n-2)-i
    for j in range(down_space):
        print(" ", end="")
    down_star = n-((n-2)-i)
    for k in range(down_star):
        print("*", end="")
    print()