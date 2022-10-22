import math


def myPrint01():
    for i in range(0, 10, 1):
        print(i)


def myPrint02(m, n):
    for j in range(n, m, -1):  # n比m大 倒著數 876
        print(j, end='')  # 不換行


def myPrint03(m):
    for j in range(0, 2 * m - 1, 1):
        print(j, end='')  # 不換行


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
        print((n - (i + 1)) * ' ' + (i + 1) * '*', end='\n')


def myDownTriangle(n):
    for i in range(n):
        print(i * ' ', end='')
        print((n - i) * '*', end='\n')


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
        print(' ' * (n - i) + (i * 2 + 1) * '*')


def printStar(n):
    print("*" * n)


def myprints(n):
    for i in range(0, n):
        print((n - (i + 1)) * '#', end='')
        getNum(i)
        print('')


def getNum(x):
    for i in range(x, -1, -1):
        print(i, end='')


def myprints2(n):
    for i in range(1, 2 * n + 1, 2):
        print(i, end='')


def myprint3(num):
    for x in range(1, num + 1):
        for y in range(num, x, -1):
            s = '({0},{1})'.format(x, y)
            print(s, end=';')
        for y in range(1, 2 * x, 1):
            s = '({0},{1})'.format(x, y)
            print(s, end=',')
        print()


# def sequence(n):
#     while n > 0:
#         print('hello %d' %n)
#         n += 1
#     print("結束了嗎")


def myStrSequence(name):
    count = 0
    for i in name:
        count += 1
        if i == 'i':
            break
        print('第%d個字是:%s' % (count, i))


def myStrSequence2(name):
    count = 0
    for i in name:
        count += 1
        if i == 'i':
            continue
        print('第%d個字是:%s' % (count, i))


"""
小考會考
1 Function 1 loop
1234
123
12
1
"""


def myloop(num):
    if num != 0:
        for i in range(num):
            print(i + 1, end='')
        print()
        myloop(num - 1)


"""
8421#
421#
21#
1
"""


def printOneRow(m, n, s, mark):
    for i in range(m, n, s):
        if mark.isdigit():
            print(i, end='')
        else:
            print(mark, end='')


def callMyRow(n):
    # 4 3 2 1
    for i in range(n, 0, -1):
        maxNum = 2 ** (i-1)
        if maxNum == 0:
            maxNum = i
        d1 = maxNum - (maxNum/2)
        d2 = n/2 #2
        d3 = n/n #1
        printOneRow(maxNum,0,d1,'1')
        printOneRow(maxNum/2,0,d2,'1')
        printOneRow(maxNum/2,0,d3,'1')
        printOneRow(maxNum,0,d3,'#')

if __name__ == '__main__':
    # myStrSequence2('chris')
    # myStrSequence('chris')
    # main1()
    # main02()
    # myPrint(5)
    # myTriangle(4)
    # myDownTriangle(5)
    # myPrintS()
    # myPyramid(5)
    # printStar(2)
    # myprints(4)
    # myprint3(4)
    # myloop(4)
    # myloop(3)
    printOneRow()
