def comaparision_of_lists(l1,l2):
    len1=len(l1)
    len2=len(l2)
    count=0
    if(len1==len2):
        for i in range(0,len1,1):
            if l1[i]==l2[i]:
                count+=1
        if count==len2:
            return True
        else:
            return False
print("Program to check if the two given lists are same")
n=int(input("Enter the number of elements of 1st list\n"))
l1=[]
print("Enter the elements")
for i in range(n):
    list=input()
    l1.append(list)
m=int(input("Enter the number of elements "))
l2=[]
print("Enter the elements")
for i in range(m):
    list2=input()
    l2.append(list2)
res=comaparision_of_lists(l1,l2)
print(res)


