'''
*       times=1 i=0 stars=1
**      times=2 i=1 stars=2
***     times=3 i=2 stars=3
****    times=4 i=3 stars=4
*****   times=5 i=4 stars=5

stars= i+1
'''

n=int(input("How many numbers "))
for i in range(n):
    num_of_stars=i+1
    for j in range(num_of_stars):
      print("*",end="")
    print()