# function to calculate the square footage of a house
def house_square_footage(le, wi):
    area = le * wi
    return f" {area} sq.ft."


# function to calculate the circumference of a circle
from math import pi

def find_circumfrence_by_diameter(d):
    c = pi * d
    return c

def find_circumfrence_by_radius(r):
    c = 2 * pi * r
    return c


# to print do this
# print(house_square_footage(20, 50))

# notes
# circumfrence = pi * diameter
# circumfrence = 2 * pi * radius