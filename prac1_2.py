'''
*****   time=1, i=0, stars=5
****    time=2, i=1, stars=4
***     time=3, i=2, stars=3
**      time=4, i=3, stars=2
*       time=5, i=4, stars=1
**      time=6, i=0, stars=2
***     time=7, i=1, stars=3
****    time=8, i=2, stars=4
*****   time=9, i=3, stars=5

up_star=n-i
down_star=i+2
'''
n=int(input("How many numbers "))

for i in range(n):
    up_star = n-i
    for j in range(up_star):
        print("*", end="")
    print()
for i in range(n-1):    #you have to reduce the input number as well
    down_star = i+2
    for k in range(down_star):
       print("*",end="")
    print()