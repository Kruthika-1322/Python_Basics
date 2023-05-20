def min_tuple(n):
    s=''
    for i in range(n):
        value=input('Enter the values')
        s=s+value
    t=tuple(s)
    print(t);
    min=t[0]
    l=len(t)
    for i in range(0,l):
        if min>t[i]:
            min=t[i]
    print('The min value is:',min)
print('Program to find the maximum value in the given list')
n=int(input('Enter the number of elements'))
min_tuple(n)