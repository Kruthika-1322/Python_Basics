def triangle(n):
    for i in range(1,n+1,1):
        for m in range(1,i+1):
            print('*',end='')
        print()
print('Program to print the right angled triangle')
n=int(input('Enter the number of rows\n'))
triangle(n)