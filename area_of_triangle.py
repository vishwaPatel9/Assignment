"""
when all the length of the sides of the triangle is known- a,b,c
semi perimeter (s) = (a + b + c) / 2
Area = square root of (s* (s-a) * (s-b) * (s-c))
"""

"""a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
s =(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is ", round(area, 2))"""

#area_of_triangle when base and height is given
height= float(input("Enter height:"))
base= float(input("Enter base:"))
area=base*height/2
print("Area of triangle is:",area)