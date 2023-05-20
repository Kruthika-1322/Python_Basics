def prime_no(n):
    sum=0
    for i in range(1,n+1,1):
        if(n%i==0):
            sum=sum+1
    if(sum==2):
        print('It is a prime number')
    else:
        print('The number is not prime number')

print('Program to find the given number is prime or not')
a=int(input('Enter the number\n'))
prime_no(a)