def fibonacci(limit):
    a,b= 1,0
    while a <limit:
        print(a,end=" ")
        a,b =b,a+b
fibonacci(10000)
    