'''
*       time=1, i=0,inside_space=0, stars=1
**      time=2, i=1,inside_space=0, stars=2
*@*     time=3, i=2,inside_space=1, stars=2
*@@*    time=4, i=3,inside_space=2, stars=2
*****   time=5, i=4,inside_space=0, stars=5


'''
n=int(input("How many numbers "))
for i in range(n):
    num_of_star=i+1
    for j in range(num_of_star):
        if(j==0 or j==num_of_star-1 or i==n-1):
            print("*",end='')
        else:
            print("@", end="")

    print()
