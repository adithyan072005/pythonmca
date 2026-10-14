n=int(input("enter number of N terms:"))
if n<=0:
    print("fibonaccci series upto ",n,"is not defined")
else:
    first=0
    second=1
    print("the first",n,"numbers in the fibonaci series:")
    print(first,",",second,end=",")
    for i in range(2,n):
        fib=first+second
        first=second
        second=fib
        if fib>n:
            break
        if i==n-1:
            print(fib,end=" ")
        else:
            print(fib,end=",")
    
