def countWord():
    fileName=input('Enter any File name present in your PC')
    no_of_words=0
    f=open(fileName)
    for line in f:
        words=line.split()
        no_of_words=no_of_words+len(words)
        print (len(words))
    print(no_of_words)
countWord()