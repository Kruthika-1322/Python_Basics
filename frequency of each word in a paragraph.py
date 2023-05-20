def count_words(string):
    string=string.split()
    j=len(string)
    for i in range(j):
        count=0
        for k in range(j):
            if(string[k]==string[i]):
                count=count+1
        print('The word {0} has appeared {1} times'.format(string[i],count))

print('Program to print the frequency of the word in a given paragraph')
string=str(input('Enter the paragrapgh\n'))
count_words(string)

    