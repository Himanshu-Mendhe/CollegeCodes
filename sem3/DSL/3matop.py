#mat add, subs, multiply, transpose
#
# 

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[9,8,7],[6,5,4],[3,2,1]]

def add(m1,m2):
    #return [[a[i][j]+b[i][j] for j in range (len(a[0]))] for i in range(len(a))]
    result = [[0 for i in range (3)]for j in range (3)]

    for a in range (len(m1[0])):
        for b in range (len(m1)):
            result [a][b] = m1[a][b] + m2[a][b]
    print (result)


def sub(m1,m2):
    result = [[0 for i in range (3)]for j in range (3)]

    for a in range (len(m1[0])):
        for b in range (len(m1)):
            result [a][b] = m1[a][b] - m2[a][b]
    print (result)

def mul (m1,m2):
    result = [[0 for i in range (len(m2[0]))]for j in range (len(m1))]

    for i in range (3):
        for j in range(3):
            for k in range (3):
                result[i][j] += m1[i][k] * m2[k][j]
    print(result)

def transpose(m):
    result = [[0 for i in range (len(m[0]))]for j in range (len(m))]
    for i in range (len(m)):
        for j in range (len(m[0])):
            result[i][j] = m[j][i]
    print (result)

add(m1,m2)
sub(m1,m2)
mul(m1,m2)
transpose(m1)