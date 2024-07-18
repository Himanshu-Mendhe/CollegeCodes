
#QUE -- Write a Python program to compute following operations on String:
#a) To display word with the longest length
#b) To determines the frequency of occurrence of particular character in the string
#c) To check whether given string is palindrome or not
#d) To display index of first appearance of the substring
#e) To count the occurrences of each word in a given string

str = " 12345  123456 67 vhk"

def longestWord () :
    wordLength = 0
    longestWordLength = 0
    indexOfLongestWord= []
    for i in range (0,len(str),1) :
        if (str[i] != ' ') :
            wordLength += 1
        
        if (wordLength >= longestWordLength):
            indexOfLongestWord.append(i)
            a = i
            longestWordLength = wordLength
  
            
        if (str[i] == " ") :
            wordLength = 0


    print(longestWordLength) 
    print(indexOfLongestWord)
    print(a)
            

longestWord()
