def area_and_perimeter(b,h,l):
    area=0.5*b*h
    perimeter=b+h+l
    print('The area and perimeter of the triangle')
    print('The area:{0} , The perimeter:{1}'.format(area,perimeter))
print('The program to find the area and perimeter of traingle')
b=float(input('Enter the breadth of the triangle'))
h=float(input('Enter the height of the triangle'))
l=float(input('Enter the length of the triangle'))
area_and_perimeter(b,h,l)
