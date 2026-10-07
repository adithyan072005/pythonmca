import operator
mydict={}
while True:
    key=input("enter a key(or'q'to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict[key]=value
print('original dictonary:',mydict)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
print("dictionary in ascending order by value:",sd)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=true))
print("dictionary in descending order by value:",sd)
