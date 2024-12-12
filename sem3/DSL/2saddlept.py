a = [[9,8,7],[6,5,4],[3,2,1]]



def start(a):
    for i in range (len(a)):
        
        min = a[i][0]
        minind = 0
        for j in range (len(a[0])):
            if (a[i][j]<min):
                min = a[i][j]
                minind = j


        called = True
        for k in range (len(a)):
            if (a[k][minind]>min):
                called = False
                break

        if (called == True):
            print("saddle pt is", min)
            return

    print("not found")
    return

start(a)