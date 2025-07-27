'''
*       time=1, i=0, stars=1
**      time=2, i=1, stars=2
***     time=3, i=2, stars=3
****    time=4, i=3, stars=4
*****   time=5, i=4, stars=5
****    time=6, i=0, stars=4
***     time=7, i=1, stars=3
**      time=8, i=2, stars=2
*       time=9, i=3, stars=1
up_stars=i+1
down_stars=n-i
'''
n=int(input("How many numbers "))

for i in range(n):
    up_star = i+1
    for j in range(up_star):
        print("*", end="")
    print()
for i in range(n):
    down_star = n-i-1
    for k in range(down_star):
       print("*",end="")
    print()