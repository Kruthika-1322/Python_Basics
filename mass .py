def mass_of_person(wt,ht):
    mass=wt/(ht*ht)
    print('The mass of the person is:',mass)

print('Program to find the mass')
wt=float(input('Enter the weight of the person'))
ht=float(input('Enter the height of the person in m'))
mass_of_person(wt,ht)
