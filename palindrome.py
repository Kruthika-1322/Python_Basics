def palindrome(n):
    return n==n[::-1]
print("Program to check whether the given string is palindropme or not")
n=str(input("Enter the string\n"))
palindrome(n)
ans=palindrome(n)
if ans:
    print('Yes it is palindrome',)
else:
    print('It is not palindrome')