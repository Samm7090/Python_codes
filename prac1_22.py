'''
*****   time=1,i=0,stars=5
*@@@*   time=2,i=1,stars=5
*@@@*   time=3,i=2,stars=5
*@@@*   time=4,i=3,stars=5
*****   time=5,i=4,stars=5

star=n
'''
n=int(input("How many numbers "))
for i in range(n):
    num_of_stars=n
    for j in range(num_of_stars):
        if(j==0 or j==num_of_stars-1 or i==0 or i==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()