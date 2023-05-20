import datetime
def date():
    x=datetime.datetime.now()
    r=x.strftime("%d-%m-%Y")
    return r
print("Program to print the current date, month,year and time ")
res=date()
print("The present year:{0}".format(date()))