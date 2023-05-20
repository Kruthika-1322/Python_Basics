def exceptions(x,y):
    try:
        z=x/y
    except ValueError as e:
        print('Error occured is',e)
        z='None'
    return z
x=input("Enter the first number")
y=input("Ente rthe second number")
res=exceptions(x,y)
print("The result is:",z)