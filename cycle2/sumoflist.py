num=[]
n=int(input("enter the number of values in list:"))
print("enter the elements to the list:")
for i in range(n):
    val=int(input())
    num.append(val)
total=0
for item in num:
    total=total+item
print("the sum of all items in the list:",total)
