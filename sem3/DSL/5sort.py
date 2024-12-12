a = [12,4,25,54,3,34,2,5,245,2453,2345.245,2435.4,34.2,24.2]

def bs(a):
    for i in range (len(a)-1):
        for j in range (len(a)-i-1):
            if (a[j]>a[j+1]):
                temp = a[j]
                a[j]=a[j+1]
                a[j+1] =temp
    print (a)

def ss(a):
    for i in range (len(a)):
        minind = i
        for j in range (i,len(a),1):
            if a[j]<a[minind] :
                minind = j

        temp = a[minind]
        a[minind]= a[i]
        a[i]= temp
    print(a) 



#bs (a)
ss(a)