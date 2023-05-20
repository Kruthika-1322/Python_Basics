from datetime import datetime
def  hours():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    return current_time
print("Program to get the current time")
print("Current Time =",hours())