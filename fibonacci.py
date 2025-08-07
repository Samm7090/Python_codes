def fibonacci(n):
    fib_seq=[]
    a=0
    b=1
    for _ in range(n):
        fib_seq.append(a)
        a,b=b,a+b
    return fib_seq

print(fibonacci(10))