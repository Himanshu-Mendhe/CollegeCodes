a = [12.31,23.44,87.67,56.75,97.65,76.45,23.12,43,56.56,98.57,99,49.47]
print (min(a))
def bucsort(a):
    buckets = len(a)
    rang = ((max(a)-min(a))/buckets)

    bucket = [[] for _ in range (len(a))]

    for i in range (len(a)):
        index = int((a[i]-min(a))/rang)
        if (index == buckets ): 
            index -=1
        bucket[index].append(a[i])
    
    sorted = []
    for j in range (buckets):
        bucket[j].sort()
        sorted += bucket[j]


    return sorted


print(bucsort(a))