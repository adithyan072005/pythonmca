clr=[]
count=int(input("enter the number of colours:"))
print("enter the colorrs:")
for x in range(count):
    color=input()
    clr.append(color)
print("first color:",clr[0],"last color:",clr[count-1])
