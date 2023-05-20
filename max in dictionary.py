def dictionary(n):
    d={}
    for i in range(0,n):
        keys=input('Enter the key')
        v=input('Enter the value')
        d.update({keys:v})
    print('The dictionary output is:', d)
    key_max=max(d.keys(),key=(lambda k:d[k]))
    key_min=min(d.keys(),key=(lambda k:d[k]))
    print('The maximum value is:',d[key_max])
    print('The minimu value is:',d[key_min])
print('Program to print the inputs in dictionary form')
n=int(input('Enter the number of elements'))
dictionary(n)
