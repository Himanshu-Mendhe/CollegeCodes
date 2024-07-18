
#QUE -- Write a Python program to compute following operations on String:
#a) To display word with the longest length
#b) To determines the frequency of occurrence of particular character in the string
#c) To check whether given string is palindrome or not
#d) To display index of first appearance of the substring
#e) To count the occurrences of each word in a given string


def longestWord () :
    wordLength = 0
    longestWordLength = 0
    lastIndexOfLongestWord= [0]

    for i in range (0,len(myStr),1) :
        if (myStr[i] != ' ') :
            wordLength += 1

            if (wordLength >= longestWordLength):
                lastIndexOfLongestWord.pop(0)
                lastIndexOfLongestWord.append(i)
                longestWordLength = wordLength

        else :
            wordLength = 0

    indexOfLongestWord = lastIndexOfLongestWord[0] - longestWordLength

    print(longestWordLength)
    print(myStr[indexOfLongestWord:lastIndexOfLongestWord[0]+1])
            
#longestWord()

def charRepetition (someChar) :
    repCount = 0
    for i in range (0,len(myStr),1) :
        if (myStr[i] == someChar) :
            repCount += 1

    print(repCount)

#charRepetition("@")

def checkPalindrome (testCase) :
    flag = False
    for i in range (0,len(testCase),1) :
        if (testCase[i] == testCase[-i-1]):
            flag = True
        else : 
            flag = False
            break

    if flag == True :
        print (testCase,"is a palindrome")   
    else :
        print (testCase,"is not a palindrome")    

#checkPalindrome("muafaum") 

def firstAppIndex (testCase) :
    for i in range (0,len(myStr),1) :
        count = 0
        for j in range (0,len(testCase),1):
            if (myStr[i+j] == testCase[j]) :
                count +=1
            else :
                break

        if (count == len(testCase)):
            print(i)
            break    

#firstAppIndex("him")




def start () :
    inp = int(input ("👀 HELLO EVERYONE!! So click the number for the corresponding tasks to perform\n1) To display word with the longest length\n2) To determines the frequency of occurrence of particular character in the string\n3) To check whether given string is palindrome or not\n4) To display index of first appearance of the substring\n5) To count the occurrences of each word in a given string"))
    if (inp == 1) :
        longestWord()
        start()
    elif (inp == 2):
        someChar = input("tell the character")
        charRepetition(someChar)
        start()
    elif (inp == 3):
        testCase = input ("give any testcase to check weather it is palindrome or not")
        checkPalindrome(testCase)
        start()
    elif (inp == 4):
        testCase = input("give the substring whose first index you want to know")
        firstAppIndex(testCase)
        start()
    elif (inp == 5):
        #do something
        print("hii")
    else :
        print("type correct response")
        start()


start()    