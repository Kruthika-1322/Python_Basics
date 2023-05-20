def numeric_value(n):
    lstn=["Zero",'One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
    for i in range(0,len(lstn)+1,1):
        if(n==i):
            print(lstn[i])
            break
print('Program to print thr numeric value')
n=int(input("Enter the number from 0-9\n"))
numeric_value(n)

