def vowels_and_constants(str):
    if((str=='a') or (str=='i') or (str=='e') or (str=='o') or (str=='u')):
        print("It is vowel")
    else:
        print('It is constant')
print('Program to find out the given character is vowels or constant')
string=input("Enter the string\n")
vowels_and_constants(string)