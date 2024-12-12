
#QUE -- Write a Python program to compute following operations on String:
#a) To display word with the longest length
#b) To determines the frequency of occurrence of particular character in the string
#c) To check whether given string is palindrome or not
#d) To display index of first appearance of the substring
#e) To count the occurrences of each word in a given string


def longestWord (myStr) :
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

    print("longest word is",myStr[indexOfLongestWord:lastIndexOfLongestWord[0]+1],"and its length is",longestWordLength)     

#longestWord()



def charRepetition (myStr, someChar) :
    repCount = 0
    for i in range (0,len(myStr),1) :
        if (myStr[i] == someChar) :
            repCount += 1

    print("Repetition count of character",someChar,"is",repCount)

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

#checkPalindrome("madam") 

def firstAppIndex (myStr,testCase) :
    for i in range (0,len(myStr),1) :
        count = 0
        for j in range (0,len(testCase),1):
            if (myStr[i+j] == testCase[j]) :
                count +=1
            else :
                break

        if (count == len(testCase)):
            print("the index of first occurrence of ",testCase,"is",i)
            break    

#firstAppIndex("him")




def start () :
    while True :
        inp = int(input ("👀 HELLO EVERYONE!! So click the number for the corresponding tasks to perform\n1) To display word with the longest length\n2) To determines the frequency of occurrence of particular character in the string\n3) To check whether given string is palindrome or not\n4) To display index of first appearance of the substring\n5) To count the occurrences of each word in a given string"))
        if (inp == 1) :
            myStr = input("write a string")
            longestWord(myStr)
        elif (inp == 2):
            myStr = input("write a string")
            someChar = input("tell the character")
            charRepetition(myStr, someChar)
        elif (inp == 3):
            testCase = input ("give any testcase to check weather it is palindrome or not")
            checkPalindrome(testCase)
        elif (inp == 4):
            myStr = input("write the string")
            testCase = input("give the substring whose first index you want to know")
            firstAppIndex(myStr,testCase)
        elif (inp == 5):
            #do something
            print("hii")
        else :
            print("type correct response")


start()    