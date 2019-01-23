"""DOCSTRING for Lab 02"""
#Wendell Yeung
#A01063806
#22 January 2019

PI = 3.14159
radius = 0
radius = float(input("Enter your radius:\n"))
calculatedCircumference = 2 * PI * radius
print("The calculated circumference is", calculatedCircumference)
calculatedArea = float(PI * radius * radius)
print("The calculated area is", calculatedArea)
double_radius = 2 * radius
double_circumference = 2 * PI * double_radius
double_area = PI * double_radius * double_radius
print("When you double the radius, the circumference increases by a factor of", (double_circumference / calculatedCircumference), "and the area increases by a factor of", (double_area / calculatedArea))