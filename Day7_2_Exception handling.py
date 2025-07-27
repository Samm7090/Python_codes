f=open("logs.txt","w")
log_data=''
operation_completed=False
while(operation_completed==False):
    try:
        num=int(input("enter the number "))
        print(num*num)
        operation_completed=True
    except Exception as e:
        log_data=log_data+str(e)+'\n'
        print("kripaya sahi sankhya daale")
f.write(log_data)
f.close()