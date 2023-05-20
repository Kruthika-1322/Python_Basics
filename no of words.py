def no_of_words(sentence):
    j=len(sentence)
    count=0
    for i in range(j):
        if(sentence[i]==' '):
            count=count+1
    return count

print('Program to count the number of words')
sentence=str(input('Enter the sentence\n'))
no_of_words(sentence)
print(no_of_words(sentence))