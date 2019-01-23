"""DOCSTRING for Lab 02"""
#Wendell Yeung
#A01063806
#22 January 2019


COVERAGE = 400
length = float(input("Enter your room length in feet. "))
width = float(input("Enter your room width in feet. "))
height = float(input("Enter your room height in feet. "))
coats = float(input("Enter the number of desired coats. "))
surface_area = 5 * (length * width * height)
coverage_needed = coats * surface_area
cans_of_paint_required = coverage_needed / COVERAGE
print("You will need", cans_of_paint_required, "cans of paint.")