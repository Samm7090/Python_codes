'''
*@@@@@@@@*      time=1, i=0,inside_space=8, stars=2
**@@@@@@**      time=2, i=1,inside_space=6, stars=4
***@@@@***      time=3, i=2,inside_space=4, stars=6
****@@****      time=4, i=3,inside_space=2, stars=8
**********      time=5, i=4,inside_space=0, stars=10

 num_of_stars=i+1
in_space=(n*2)-(2*i)-2
 num_of_stars=i+1
'''
n=int(input("How many numbers "))
for i in range(n):
    num_of_stars=i+1
    for j in range(num_of_stars):
      print("*",end="")
    in_spaces = (n*2)-(2*i)-2
    for k in range(in_spaces):
       print(" ",end="")
    num_of_stars = i+1
    for l in range(num_of_stars):
       print("*",end="")
    print()