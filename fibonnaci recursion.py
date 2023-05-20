def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

print("Program to print the fibonnaci series using recursion")
l=[]
n = int(input("Enter number of terms:"))
for i in range(n):
    res=fibonacci(i)
    l.append(res)
print(l)

