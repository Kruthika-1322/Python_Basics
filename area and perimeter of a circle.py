import math
def area_and_perimeter(r):
    area=math.pi*r*r
    perimeter=2*math.pi*r
    print('The area and perimeter of the given circle is:')
    print('Area=\n',area)
    print('Perimeter\n',perimeter)
print('Program to find the perimeter and area of the circle')
r=float(input('Enter the radius of the circle'))
area_and_perimeter(r)