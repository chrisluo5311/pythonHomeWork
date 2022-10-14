def myPrint01():
    for i in range(0, 10, 1):
        print(i)
def myPrint02(m, n):
    for j in range(n, m, -1): # n比m大 倒著數 876
        print(j, end='') #不換行
def myPrint03(m):
    for j in range(0, 2*m-1, 1):
        print(j, end='') #不換行
def main1():
    num = 5
    # myPrint01()
    # myPrint02(num, 8)
    myPrint03(num)
    # print() #預設換行


def myPrint04(listData):
    for i in listData:
        print(i)
def main02():
    listData = ['a', 'b', 'c', 'd']
    myPrint04(listData)

def myPrint(n):
    for i in range(n):
        print('*', end='')

def myTriangle(n):
    for i in range(n):
        print((n-(i+1))*' ' + (i+1)*'*',end='\n')

def myDownTriangle(n):
    for i in range(n):
        print(i*' ',end='')
        print((n-i)*'*',end='\n')

def myPrintS():
    for i in range(1, 4):
        myPrint(i)
    print()

"""
#     *
#    ***
#   *****
#  *******
# *********
"""
def myPyramid(n):
    for i in range(n):
        print(' '*(n-i) + (i*2+1)*'*')


def printStar(n):
    print("*"*n)


if __name__ == '__main__':
    # main1()
    # main02()
    # myPrint(5)
    # myTriangle(4)
    # myDownTriangle(5)
    # myPrintS()
    # myPyramid(5)
    printStar(2)




