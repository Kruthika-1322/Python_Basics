print('Program to LCM of a nubers')
m=int(input("Enter the number\n"))
n=int(input("Enter the second\n"))
k=2
if m>n:
    
    for i in range(1,20,1):
        if((m%i==0) and (n%i==0)):
            k=i*k
    print(k)    
        
else:
    for i in range(1,20,1):
        if((m%i==0) and (n%i==0)):
             k=i*k
    print(k)
       
    
    

    
    
