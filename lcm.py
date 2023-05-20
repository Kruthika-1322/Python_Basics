print("Enter the number")
a=int(input("Enter the first number"))
b=int(input('Enter the second number'))

if a>b:
    m=a
    for i in range (1,a,1):
        m=m*i
        if ((m%a==0) and (m%b==0)):
            print('{0} is lcm of the given numbers'.format(m))
            break
else:
    m=b
    for i in range (1,b,1):
        m=m*i
        if ((m%a==0) and (m%b==0)):
            print('{0} is lcm of the given numbers'.format(m))
            break
