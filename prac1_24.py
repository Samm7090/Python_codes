'''
**********      time=1, i=0,inside_space=0, stars=10
****@@****      time=2, i=1,inside_space=2, stars=8
***@@@@***      time=3, i=2,inside_space=4, stars=6
**@@@@@@**      time=4, i=3,inside_space=6, stars=4
*@@@@@@@@*      time=5, i=4,inside_space=8, stars=2
**@@@@@@**      time=7, i=0,inside_space=6, stars=4
***@@@@***      time=8, i=1,inside_space=4, stars=6
****@@****      time=9, i=2,inside_space=2, stars=8
**********      time=10,i=3,inside_space=0, stars=10

up_stars= n-i
up_in_space=2*i
up_stars= n-i
down_stars=i+1
down_in_space=(n*2)-(2*i)-2
down_stars=i+1
'''
n=int(input("How many numbers "))
for i in range(n-1):
    up_stars= n-i
    for j in range(up_stars):
       print("*",end="")
    up_in_spaces = 2*i
    for j in range(up_in_spaces):
        print(" ", end="")
    up_stars = n-i
    for k in range(up_stars):
        print("*", end="")
    print()
for i in range(n):
    down_stars=i+1
    for j in range(down_stars):
      print("*",end="")
    down_in_spaces = (n*2)-(2*i)-2
    for k in range(down_in_spaces):
       print(" ",end="")
    down_stars = i+1
    for l in range(down_stars):
       print("*",end="")
    print()