def min_list(n):
    lst=[]
    for i in range(n):
        list=int(input('Enter the values'))
        lst.append(list)
    print(lst)
    min=lst[0]
    l=len(lst)
    for i in range(0,l):
        if min>lst[i]:
            min=lst[i]
    print('The min value is:',min)
print('Program to find the maximum value in the given list')
n=int(input('Enter the number of elements'))
max_list(n)