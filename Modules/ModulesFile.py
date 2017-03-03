var1 = "variable local"

var2 = 897

def nums(*arrayNums):
    a = 0
    for i in arrayNums:

        a += i

    return a

def numsArgs(v1,v2, v3, v4):

    print('Valor:' + v1)
    print('Valor:' + v2)
    print('Valor:' + v3)
    print('Valor:' + v4)

def keyValue (**keyValues):

    for i, j in keyValues.items():

        print (i + " : " + j)

def arrayKeyValue (a,b,c):

    print(a)
    print(b)
    print(c)