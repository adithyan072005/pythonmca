calc_square_area=lambda sidelength:sidelength**2
calc_rect_area=lambda length,width:length*width
calc_tri_area=lambda base,height:0.5*base*height

sq=int(input("enter the side of sqaure"))
print("enter the base and height of triangle:")
ht=int(input("height:"))
b=int(input("base:"))

print("enter the length and breadth of triangle:")
l=int(input("length:"))
b=int(input("breadth:"))

sqaurearea=calc_square_area(sq)
print("area of sqaure:",sqaurearea)

triarea=calc_tri_area(b,ht)
print("area of triangle:",triarea)

rectarea=calc_rect_area(l,b)
print("area of rectangle:",rectarea)
