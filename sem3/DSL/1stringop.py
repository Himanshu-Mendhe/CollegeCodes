a = "hii this is himanshuhii mendhe and i hiiam doing this hii for the college practicals"


def longest(a):
    length = 0
    count = 0

    for i in range (len(a)):
        
        if (a[i] == " "):
            count = 0
            continue
        
        count+=1
        if (count > length):
            wordint = i
            length = count

    print (a[wordint-length+1:wordint+1])   


def fre(key, a):
    size = len(key)
    count = 0
    for i in range (len(a)):
        if (key == a[i:i+size]):
            count+=1
    print (count)
    return count

def pal (a):
    for i in range ( len(a)):
        if (a[i]!=a[-i-1]):
            print ("not palindrome")
            return 
    print ("is pallindrome")

#similarly all the logics
# for the word occurrence create two array one for the words and other for the word length. stop while the space comes 

longest(a)
fre("hii", a)
pal("madaam")