def min_set(n):
    es=set()
    for i in range(n):
        ems=int(input('Enter the values'))
        es.add(ems)
    print(es)

    print('The max value of the given set is',min(es))
print('Program to find the maximum value in the given list')
n=int(input('Enter the number of elements'))
min_set(n)