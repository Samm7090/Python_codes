'''
1.Add
2.Intersection
3.Union
4,Difference
5Symmetric Difference
6.Exit
'''
A=set()
B=set()
choice=0
while(choice!=6):
    print("1.Add set")
    print("2.Intersection set")
    print("3.Union set")
    print("4.Difference ")
    print("5.Symmetric Difference")
    print("6.Exit")
    choice=int(input("Enter the choice "))
    if(choice==1):
        setA = int(input("How many elements to add in A"))
        setB = int(input("How many elements to add in B"))
        for i in range(setA):
            element=input("Enter the elements to add in A ")
            A.add(element)
        print(A)
        for j in range(setB):
            element=input("Enter the elements to add in B ")
            B.add(element)
        print(B)
    elif(choice==2):
        print(A.intersection(B))
    elif(choice==3):
        print(A.union(B))
    elif(choice==4):
        print(A.difference(B))
    elif(choice==5):
        print(A.symmetric_difference(B))
    elif(choice==6):
        print("thankyou")
    else:
        print("Invalid input")

