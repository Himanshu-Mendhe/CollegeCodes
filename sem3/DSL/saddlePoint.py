# To find the saddle point of a matrix
M = []
flag = 'notCalled'
def matrixInput(rows,column):
    global M,flag
    M= []
    for i in range(rows):
        row = []
        for j in range(column):
            val = int(input(f"Enter the matrix number for position ({i+1},{j+1}): "))
            row.append(val)
        M.append(row)
    flag = 'called'
    return M

def showMatrix():
    print ("The input Matrix is: \n")
    for i in M :
        for j in i :
            print (j,"  ",end=' ')   


def saddlePoint(M):
    flag2 = False
    for i in range(len(M)):
        min = M[i][0]
        indexOfRow = i
        indexOfCol = 0
        for j in range(len(M[0])):
            if (M[i][j] < min) :
                min = M[i][j]
                indexOfRow = i
                indexOfCol = j
        for k in range(len(M)):
            if (M[k][indexOfCol]>min):
                flag2 = False
                break
            else:
                flag2 = True
                saddlePoint = min
    if flag2 == True :
        print("the saddle point is ", saddlePoint,indexOfRow,indexOfCol)
    else :
        print("no saddle point in this matrix")
        

def start () :
    while True:
        startPrompt = int(input("Hello everyone this is the code to find the saddle point of the matrix.\nPress 1 for entering the input of matrix.\nPress 2 to show the matrix.\nPress 3 to find the saddle point of the input matrix "))

        if (startPrompt == 1) :
            print("You clicked option 1 i.e to enter the matrix")
            rows = int(input("please enter the number of rows you want to keep in the matrix: "))
            column = int(input("please enter the number of column you want to keep in the matrix: "))
            matrixInput(rows,column)
        elif (startPrompt == 2):
            print("You clicked option 2 i.e to show your matrix")
            if (flag == 'notCalled'):
                print("oops!! seems you have not given the input of matrix.\nplease select the option 1 to give the input of the matrix and then look the matrix")
            elif (flag == 'called'):
                showMatrix()
        elif (startPrompt == 3):
            print("You clicked option 3 i.e to show the saddle point of your matrix")
            if (flag == 'notCalled'):
                print("oops!! seems you have not given the input of matrix.\nplease select the option 1 to give the input of the matrix and then find the saddle point")
            elif (flag == 'called'):
                saddlePoint(M)
        else :
            print("please enter the valid input number")
start()