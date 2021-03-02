# take all the chars that I got and then put them in li
def readcharsfromuser():
    li=[]
    print("please insert chars for done insert 0")
    while(1):
        char=input("insert char")
        if char=='0':
            break
        li.append(char)
    return li
#read all the word in words.txt to a list .
def readWordsFromFile(fileName):
    wordList = []
    try:
        with open(fileName, "r") as f:
            for line in f:
                wordList.append(line)
    except:
        print(f'Something Went Wrong')
    return wordList

#check if the player is correct
if __name__ == '__main__':
    liRes = []
    list1=readcharsfromuser()
    li = readWordsFromFile("words.txt")
    for word in li:
        count = 0
        for ch in list1:
            if ch in word:
                count += 1

        if count == len(list1):
            liRes.append(word)

    for word in liRes:
        print(word)
    if len(liRes) == 0:
        print("Try again")