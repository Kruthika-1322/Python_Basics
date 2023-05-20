def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)

print('Program to find the factorial using recursion')
n=int(input('Enter the number\n'))
factorial(n)
print('The factorial of given number is',factorial(n))
