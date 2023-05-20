def fibonnaci_series(n):
    count=0
    a=0
    b=1
    sum=0
    l=[]
    while count<=n:
        count+=1
        a=b
        b=sum
        sum=a+b
        l.append(sum)
    return l
print("Program to find the fibonnaci series")
n=int(input("Enter the number\n"))
fibonnaci_series(n)
res=fibonnaci_series(n)
print(res)