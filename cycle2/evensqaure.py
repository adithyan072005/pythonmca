result=[]
start=int(input("enter the starting range(four-digit number):"))
end=int(input("enter the end range(four-digit  number):"))
if start<1000 or end>9999 or start>end:
    print("invlid range,please  enter a valid four digit range")
else:
    for num in range(start,end+1):
        if num%2==0:
            root=int(num**0.5)
            if root*root==num:
                result.append(num)
print("perfect four digit even sqaured number is the given range:")
print(result)
            
