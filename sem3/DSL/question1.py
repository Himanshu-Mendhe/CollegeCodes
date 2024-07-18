
#QUE -- Write a Python program to compute following operations on String:
#a) To display word with the longest length
#b) To determines the frequency of occurrence of particular character in the string
#c) To check whether given string is palindrome or not
#d) To display index of first appearance of the substring
#e) To count the occurrences of each word in a given string

str = "hii my name is himanshu k mendhe and i am struwafdq????!@!@"

def longestWord () :
    wordLength = 0
    longestWordLength = 0
    lastIndexOfLongestWord= [0]

    for i in range (0,len(str),1) :
        if (str[i] != ' ') :
            wordLength += 1

            if (wordLength >= longestWordLength):
                lastIndexOfLongestWord.pop(0)
                lastIndexOfLongestWord.append(i)
                longestWordLength = wordLength

        else :
            wordLength = 0

    indexOfLongestWord = lastIndexOfLongestWord[0] - longestWordLength

    print(longestWordLength)
    print(str[indexOfLongestWord:lastIndexOfLongestWord[0]+1])
            
#longestWord()


def charRepetition (someChar) :
    repCount = 0
    for i in range (0,len(str),1) :
        if (str[i] == someChar) :
            repCount += 1

    print(repCount)

#charRepetition("@")