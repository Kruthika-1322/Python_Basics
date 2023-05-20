def factorial(n):
    if(n>0):
        fact=1
        for i in range(1,n+1,1):
            fact=fact*i
        print('The factorial of given number:',fact)
    else:
        print('Enter the positive number')
    
print('Program to find the factorial of the given number')
a=int(input('Enter the number'))
factorial(a)