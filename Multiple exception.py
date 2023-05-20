def multiple():
    try:
        x = int(input("Enter the first number"))
        y = int(input("Ente rthe second number"))
        z=x/y
    except ZeroDivisionError as e:
        print("Zero Division error occured:")
        z='None'
    except ValueError as e:
        print("Value error occured:")
        z="None"
    return z

res= multiple()
print("The result is:",res)