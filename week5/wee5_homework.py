"""
17
* 請使用funtion跟迴圈，每一個function裡面只使用一層迴圈 (while loop 或 for loop) *
* 亦即一個 function 不要有巢狀迴圈 *
繪製三種不同的圖形
圖形請考範例測資
---------------------------------------------------
輸入說明 :
第一行，輸入整數 1 or 2 or 3，代表接下來要畫的圖形種類
第一種圖形為 直角三角形 (參考 範例輸出 1、範例輸出 2)
第二種圖形為 正三角形 (參考 範例輸出 3、範例輸出 4)
第三種圖形為 倒三角形 (參考 範例輸出 5、範例輸出 6)
第二行，輸入整數 N ，代表這個圖形有N行
輸出說明 :
根據輸入，畫出對應的圖形
輸出圖形為數字+底線
此題不用考慮第一行輸入1,2,3以外的情況
---------------------------------------------------
範例輸入 1:
1
5
範例輸出 1:
1
121
12321
1234321
123454321
---------------------------------------------------
範例輸入 2:
1
8
範例輸出 2:
1
121
12321
1234321
123454321
12345654321
1234567654321
123456787654321
---------------------------------------------------
範例輸入 3:
2
4
範例輸出 3:
___1___
__121__
_12321_
1234321
---------------------------------------------------
範例輸入 4:
2
6
範例輸出 4:
_____1_____
____121____
___12321___
__1234321__
_123454321_
12345654321
--------------------------------------------------
範例輸入 5:
3
3
範例輸出 5:
12321
_121_
__1__
---------------------------------------------------
範例輸入 6:
3
4
範例輸出 6:
1234321
_12321_
__121__
___1___
"""


def myPyramid():
    types = int(input())
    lines = int(input())
    if types == 1:
        myRightTriangle(lines)
    elif types == 2:
        myIsoTriangle(lines)
    else:
        myUpsideDownTriangle(lines)


def myRightTriangle(lines):
    for i in range(lines):
        if i > 0:
            print("")
        printForward(i + 1)
        printBackward(i + 1)


def myIsoTriangle(lines):
    maxNum = lines
    for i in range(lines):
        if i > 0:
            print("")
        printDividersDown(maxNum)
        printForward(i + 1)
        printBackward(i + 1)
        printDividersDown(maxNum)
        maxNum -= 1


def myUpsideDownTriangle(lines):
    maxNum = lines
    for i in range(lines):
        if i > 0:
            print("")
        printDividersUp(i)
        printForward(maxNum)
        printBackward(maxNum)
        printDividersUp(i)
        maxNum -= 1


def printDividersDown(maxnum):
    for i in range(maxnum - 1, 0, -1):
        print("_", end="")


def printDividersUp(maxnum):
    for i in range(maxnum):
        print("_", end="")


def printForward(maxnum):
    for i in range(maxnum):
        print("%d" % (i + 1), end="")


def printBackward(maxnum):
    for i in range(maxnum - 1, 0, -1):
        print("%d" % i, end="")


"""
18 -
* 請使用funtion跟迴圈，每一個function裡面只使用一層迴圈 (while loop 或 for loop) *
* 亦即一個 function 不要有巢狀迴圈 *
繪製三種不同的圖形
圖形請考範例測資
---------------------------------------------------
輸入說明 :
第一行，輸入整數 1 or 2 or 3，代表接下來要畫的圖形種類
第一種圖形為 朝右邊斜的平行四邊形 (參考 範例輸出1、範例輸出2)
第二種圖形為 朝左邊斜的平行四邊形 (參考 範例輸出3、範例輸出4)
第三種圖形為 沙漏型 (參考 範例輸出5)
第二行，輸入整數 N ，代表這個圖形有N行
輸出說明 :
根據輸入，畫出對應的圖形
輸出圖形為數字+底線
若輸出第三種圖形時，整數N不是奇數，則改為輸出ERROR，並結束程式 (不必輸出圖形)
此題不用考慮第一行輸入1,2,3以外的情況
---------------------------------------------------
範例輸入 1:
1
5
範例輸出 1:
____12345
___54321_
__12345__
_54321___
12345____
---------------------------------------------------
範例輸入 2:
1
8
範例輸出 2:
_______12345678
______87654321_
_____12345678__
____87654321___
___12345678____
__87654321_____
_12345678______
87654321_______
---------------------------------------------------
範例輸入 3:
2
5
範例輸出 3:
54321____
_12345___
__54321__
___12345_
____54321
---------------------------------------------------
範例輸入 4:
2
8
範例輸出 4:
87654321_______
_12345678______
__87654321_____
___12345678____
____87654321___
_____12345678__
______87654321_
_______12345678
---------------------------------------------------
範例輸入 5:
3
7
範例輸出 5:
4321234
_32123_
__212__
___1___
__212__
_32123_
4321234
---------------------------------------------------
範例輸入 6:
3
4
範例輸出 6:
ERROR
"""


def myParallel():
    types = int(input())
    lines = int(input())
    if types == 1:
        rightParallel(lines)
    elif types == 2:
        leftParallel(lines)
    else:
        middleParallel(lines)


def rightParallel(lines):
    maxNum = lines
    for i in range(lines):
        if i > 0:
            print("")
        printDividersDown(maxNum)
        if i % 2 == 0:
            printNums(lines, 0)
        else:
            printNums(lines, 1)
        printDividersUp(i)
        maxNum -= 1


def leftParallel(lines):
    maxNum = lines
    for i in range(lines):
        if i > 0:
            print("")
        printDividersUp(i)
        if i % 2 == 0:
            printNums(lines, 1)
        else:
            printNums(lines, 0)
        printDividersDown(maxNum)
        maxNum -= 1


def middleParallel(lines):
    if lines % 2 == 0:
        print("ERROR")
        return
    maxNum = int((lines / 2) + 1)
    middleNum = int(lines / 2)
    middleStart = 2
    for i in range(lines):
        if i > 0:
            print("")
        if i <= middleNum:
            printDividersUp(i)
            printNums(maxNum, 1)
            printMiddleUpNums(maxNum)
            printDividersUp(i)
            maxNum -= 1
        else:
            printDividersDown(middleNum)
            printNums(middleStart, 1)
            printMiddleUpNums(middleStart)
            printDividersDown(middleNum)
            middleNum -= 1
            middleStart += 1


def printMiddleUpNums(maxnum):
    for i in range(2, maxnum + 1):
        print(i, end="")


def printNums(maxnum, turn):
    if turn == 0:
        for i in range(maxnum):
            print(i + 1, end="")
    else:
        for i in range(maxnum, 0, -1):
            print(i, end="")


def printDividersUp(maxnum):
    for i in range(maxnum):
        print("_", end="")


def printDividersDown(maxnum):
    for i in range(maxnum - 1, 0, -1):
        print("_", end="")


"""
19 -
魚很可愛，這麼可愛的動物，怎麼可以吃牠
現在題目給魚的大小，請你畫出這條魚
魚由身體 (菱形) 跟 尾巴 (三角形) 兩個部分組成
身體的高度為N
尾巴的高度為(N-2)
身體部分使用*號，尾巴部分使用+號
---------------------------------------------------
輸入說明 :
第一行，輸入整數 N (3 <= N <= 100) ， 代表魚的大小
輸出說明 :
輸出大小為N的魚 (魚的圖形請參考範例測資)
如果N為偶數，請輸出ERROR，並結束程式 (不用輸出圖形)
---------------------------------------------------
範例輸入 1:
3
範例輸出 1:
  *
*****+
  *
---------------------------------------------------
範例輸入 2:
5
範例輸出 2:
    *
  *****    +
*********+++
  *****    +
    *
---------------------------------------------------
範例輸入 3:
9
範例輸出 3:
        *
      *****            +
    *********        +++
  *************    +++++
*****************+++++++
  *************    +++++
    *********        +++
      *****            +
        *
---------------------------------------------------
範例輸入 4:
4
範例輸出 4:
ERROR
"""


def myFish():
    n = int(input())
    if n % 2 == 0:
        print("ERROR")
    else:
        maxNum = n * 2 - 1
        tailMax = n - 2
        myBody(n, maxNum, tailMax)


def myBody(lines, maxnum, tailmax):
    middlePoint = int(lines / 2)
    spaceIndex = lines
    middleSpaceStart = 2
    starIndex = 1
    plusIndex = 1
    middlePlusStart = tailmax - 2
    if middlePlusStart < 0:
        middlePlusStart = 0
    for i in range(lines):
        if i > 0:
            print("")
        if i <= middlePoint:
            printSpaceDown(spaceIndex)
            printStar(starIndex)
            printSpaceDown(spaceIndex * 2 - 1)
            if i != 0:
                printPlus(plusIndex)
                plusIndex += 2
            spaceIndex -= 2
            starIndex += 4
        else:
            maxnum -= 4
            printSpaceUp(middleSpaceStart)
            printStar(maxnum)
            printSpaceUp(middleSpaceStart * 2)
            printPlus(middlePlusStart)
            middleSpaceStart += 2
            middlePlusStart -= 2


def printPlus(maxnum):
    for i in range(maxnum):
        print("+", end="")


def printStar(maxnum):
    for i in range(maxnum):
        print("*", end="")


def printSpaceDown(maxnum):
    for i in range(maxnum - 1, 0, -1):
        print(" ", end="")


def printSpaceUp(maxnum):
    for i in range(maxnum):
        print(" ", end="")


"""
20 -
給一個正整數 (2 <= N <= 10000)，請找出2~N之間所有質數的總和
---------------------------------------------------
輸入說明 :
第一行，輸入整數 N (2 <= N <= 10000)
輸出說明 :
輸出 2~N 之間所有質數的總和
---------------------------------------------------
範例輸入 1說明 :
2
範例輸出 1說明 :
2 (2~2之間的質數共有2，因此總和為2)
---------------------------------------------------
範例輸入 2說明 :
100
範例輸出 2說明 :
1060 (2~100之間的質數共有[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]，總和為1060)
--------------------------------------------------
範例輸入 1:
2
範例輸出 1:
2
---------------------------------------------------
範例輸入 2:
100
範例輸出 2:
1060
---------------------------------------------------
範例輸入 3:
10000
範例輸出 3:
5736396
"""


def sumPrimeNum():
    n = int(input())
    numList = [2]
    for i in range(3, n + 1):
        numList.append(i)

    newSumList = []
    for j in numList:
        if j == 2:
            newSumList.append(j)
        elif isPrimeNum(j):
            newSumList.append(j)

    sumPrime = 0
    for k in newSumList:
        sumPrime += k
    print(sumPrime)


def isPrimeNum(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    myPyramid()
    # myParallel()
    # myFish()
    # sumPrimeNum()
