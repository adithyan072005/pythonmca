year=2026
year2=int(input("Enter the year:"))
print("Leap year between",year,"and",year2,"are:")
for i in range(year,year2+1):
    if(i%4==0 and i%100!=0)or(i%400==0):
        print(i," ")
