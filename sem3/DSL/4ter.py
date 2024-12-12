#ternary search

arr = [1,2,3,4,23,122,233,244,2314,32523,23532]

def fun(a, b, arr, key):
    m1 = a+((b-a)//3)
    m2 = b-((b-a)//3)

    if (a>b):
        print ('not found')
        return

    if (key == arr[m1]):
        print ("fount ", m1)
        return
    if (key == arr[m2]):
        print ("fount ", m2)
        return

    if (key<arr[m1]):
        fun(a, m1-1, arr, key)
    elif (key>arr[m2]):
        fun(m2+1, b, arr, key)
    else:
        fun (m1+1, m2-1, arr, key)


fun (0,10,arr, 233)