def execeptions(x,y):
    try:
        z=x/y
    except ZeroDivisionError as e:
        z='None'
    return z
x=int(input ("Enter the first number"))
y=int(input("Enter the second number"))
execeptions(x,y)
res=execeptions(x,y)
print("The result is:",res)
