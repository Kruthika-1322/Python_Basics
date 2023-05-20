print("Program to find GCD ")
a=int(input("Eter the first number"))
b=int(input("Enter the second number"))
if(a>b):
    
    for i in range (1,a,1):
        if((a%i==0)&(b%i==0)):
            k=i

    print('{0} is the GCD of two numbers'.format(k))
else:
    for i in range (1,b,1):
        
        if((a%i==0)&(b%i==0)):
           k=i
           
print('{0} is the GCD of two numbers'.format(k))
    
            
