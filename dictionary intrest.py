def dictionary(n):
    d={}
    for i in range(0,n):
        k=input('Enter the key')
        v=input('Enter the value')
        d.update({k:v})
    print('The dictionary output is:', d)
print('Program to print the inputs in dictionary form')
n=int(input('Enter the number of elements'))
dictionary(n)
