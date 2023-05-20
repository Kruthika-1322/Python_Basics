def greetings(time):
    if time>=6 and time<12:
        return "Good Morning"
    elif time>12 and time<16:
        return "Good Afternoon"
    elif time>=16 and time<17:
        return "Good Evening"
    else:
        return "Good night"
print("Program to print the greetings according to time")
time=float(input("enter the time in format 00.00(hours.minutes)\n"))
greetings(time)
res=greetings(time)
print(res)