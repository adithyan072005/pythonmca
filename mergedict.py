mydict={}
print("enetr elements of first dict")
while True:
    key=input("enter a key(or'q'to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict[key]=value
mydict1={}
print("enetr elements of second dict")
while True:
    key=input("enter a key(or'q'to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict1[key]=value
print(mydict1)
