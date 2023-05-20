print("To find out maximum number when 3 nos")
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
if ((a>b) & (a>c)):
    print("{0} is largest of all".format(a))
elif b>c:
    print("{0} is largest of all".format(b))
else:
    print('{0} is largest of all'.format(c))
          
