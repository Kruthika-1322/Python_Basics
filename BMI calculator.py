def BMI(wt,ht):
    mass=wt/(ht*ht)
    if(mass<=18.5):
        print('Underweight')
    elif(mass>18.5 and mass<=24.9):
        print('Normal weight')
    elif(mass==25 and mass<=29.9):
        print('Over weight')
    else:
        print('Obsity')

print('Program to find the mass')
wt=float(input('Enter the weight of the person'))
ht=float(input('Enter the height of the person in m'))
BMI(wt,ht)
