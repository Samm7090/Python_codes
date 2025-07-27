'''
*****   times=1 i=0 stars=5
*@@*    times=2 i=1 stars=2
*@*     times=3 i=2 stars=2
**      times=4 i=3 stars=2
*       times=5 i=4 stars=1

'''
n=int(input("How many stars "))
for i in range(n):
    num_of_stars=n-i
    for j in range(num_of_stars):
        if(j==0 or j==num_of_stars-1 or i==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()