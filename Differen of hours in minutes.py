def diff_hours(time1,time2):
    len1=len(time1)
    d=':'
    t=time1.split(d)
    t2=time2.split(d)
    for i in range(len1):
        if(time1[i]==':' and time2[i]==':'):
            t=int(t)
            t2=int(t2)
            h=t[1]-t2[1]
            m=t[2]-t2[2]
            s=t[3]-t2[3]
            print("The difference is:{0}:{1}:{2}".format(h,m,s))
            break

print("Program to print the difference in time ")
time1=input("Enter the time in the format:HH:MM:SS\n")
time2=input("Enter the time in the format:HH:MM:SS\n")
diff_hours(time1,time2)