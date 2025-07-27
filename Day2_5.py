'''
@@@@*           time=1, i=0,start_space=4, stars=1
@@@*@*          time=2, i=1,start_space=3, stars=2
@@*@*@*         time=3, i=2,start_space=2, stars=3
@*@*@*@*        time=4, i=3,start_space=1, stars=4
*@*@*@*@*       time=5, i=4,start_space=0, stars=5

space=n-i-1
star=i+1
'''
n=int(input("How many numbers "))

for i in range(n):
    num_of_spaces = n-i-1
    for j in range(num_of_spaces):
       print(" ",end="")
    num_of_stars = i+1
    for k in range(num_of_stars):
       print("*",end=" ")
    print()