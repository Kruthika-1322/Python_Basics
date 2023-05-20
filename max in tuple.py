def max_tup(n):
    s=''
    for i in range(n):
        tu=input('Enter the values')
        s=s+tu
    t=tuple(s)
    print(t)
    maxi=t[0]
    l=len(t)
    for i in range(0,l):
        if maxi<t[i]:
            maxi=t[i]
    print('The max value is:',maxi)
print('Program to find the maximum value in the given tuppel')
n=int(input('Enter the number of elements'))
max_tup(n)