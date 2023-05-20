def vowels_and_constants(string):
    count=0
    count1=0
    j=len(string)
    for i in range(j):
        if((string[i]=='a') or (string[i]=='i') or (string[i]=='e') or (string[i]=='o') or (string[i]=='u') or (string[i]=='A') or (string[i]=='E') or (string[i]=='I') or (string[i]=='O') or (string[i]=='U')):
            count=count+1
        else:
            count1=count1+1
    print(" The total number of vowels:{0}\n The total number of consonants:{1}".format(count,count1))
print('Program to find out the number of vowels and consonants in the given sentence')
string=input("Enter the sentence\n")
vowels_and_constants(string)