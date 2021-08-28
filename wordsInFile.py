def countWordsFromFile():
    print("File name is File.txt")
    fileName=input("Enter the File Name:- ")

    numberOfWords=0

    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number Of Words ")
    print(numberOfWords)

countWordsFromFile()