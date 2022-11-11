"""
21.
繪製星星與數字的複合圖形，輸入一整數(1 <= N <= 9) 代表此圖形有N*2行。
如果N超出範圍(N < 1或N > 10)，請輸出ERROR並結束程式(不需輸出圖形)。
每行輸出多一個星號，且每行多一個數字，到第N行時則開始遞減。
例如:
N = 9
########* 1
#######** 12
######*** 123
#####**** 1234
####***** 12345
###****** 123456
##******* 1234567
#******** 12345678
********* 123456789
987654321 *********
#98765432 ********
##9876543 *******
###987654 ******
####98765 *****
#####9876 ****
######987 ***
#######98 **
########9 *
-------------------------------------------------------------------------------------------------
輸入說明:
第一行輸入整數N (1 <= N <= 9)
輸出說明:
根據輸入，畫出對應的圖形。
輸出的圖形包含井字號、星號以及數字。
如果N < 1或N > 10，請輸出ERROR。
-------------------------------------------------------------------------------------------------
範例輸入 1:
2
範例輸出 1:
#* 1
** 12
21 **
#2 *
-------------------------------------------------------------------------------------------------
範例輸入 2:
5
範例輸出 2:
####* 1
###** 12
##*** 123
#**** 1234
***** 12345
54321 *****
#5432 ****
##543 ***
###54 **
####5 *
-------------------------------------------------------------------------------------------------
範例輸入 3:
9
範例輸出 3:
########* 1
#######** 12
######*** 123
#####**** 1234
####***** 12345
###****** 123456
##******* 1234567
#******** 12345678
********* 123456789
987654321 *********
#98765432 ********
##9876543 *******
###987654 ******
####98765 *****
#####9876 ****
######987 ***
#######98 **
########9 *
-------------------------------------------------------------------------------------------------
範例輸出 4:
10
範例輸出 4:
ERROR
-------------------------------------------------------------------------------------------------
範例輸入 5:
0
範例輸出 5:
ERROR
"""


def drawStarsAndNums():
    n = int(input())
    if n < 1 or n > 9:
        print("ERROR")
    else:
        tNum = n
        totalLine = n * 2
        middleLine = n - 1
        for i in range(totalLine):
            if i <= middleLine:
                for j in range(tNum - (i + 1), 0, -1):
                    print('#', end='')
                for k in range(i + 1):
                    print('*', end='')
                print(' ', end='')
                for l in range(i + 1):
                    print(l + 1, end='')
                print()
            else:
                for m in range(i - tNum):
                    print('#', end='')
                for o in range(tNum, i - middleLine - 1, -1):
                    print(o, end='')
                print(' ', end='')
                for p in range(totalLine - i):
                    print('*', end='')
                print()
"""
22.
今天小明想要畫出一個圖形，圖形是沙漏與蝴蝶結的複合形狀
現在給予一個正整數N，N為圖形高度，範圍為 (4 <= N <= 30)
當N為偶數或是超出範圍的情況則須輸出Error並結束程式(不須輸出圖形)
當N為奇數的情況則正常輸出圖形
圖形由星號和底線組成，且星號為蝴蝶結的形狀、底線為沙漏的形狀
每一行使用星號做開頭與結尾，中間由底線填滿
每一行星號有(2n-1) * 2個、底線有N * 2 - (2n-1) * 2個
圖形可分成上半段和下半段
上半段為第1行到第 (N // 2 + 1) 行
下半段為第 (N // 2 + 2) 行到第 N 行
上半段的星號數量由上而下遞增，底線數量由上而下遞減
下半段的星號數量由上而下遞減，底線數量由上而下遞增
例如N = 9
上半段則為第1行到第5行的複合圖形，下半段則為第6行到第9行
則輸出圖形為：
*________________*
***____________***
*****________*****
*******____*******
******************
*******____*******
*****________*****
***____________***
*________________*
-------------------------------------------------------------------------------------------------
輸入說明：
第一行輸入正整數N (4 <= N <= 30)，代表圖形的大小
輸出說明：
輸出沙漏與蝴蝶結的複合圖形，大小為N
當N為偶數或是超出範圍時，輸出Error並結束程式(不須輸出圖形)
-------------------------------------------------------------------------------------------------
範例輸入1：
5
範例輸出1：
*________*
***____***
**********
***____***
*________*
-------------------------------------------------------------------------------------------------
範例輸入2：
7
範例輸出2：
*____________*
***________***
*****____*****
**************
*****____*****
***________***
*____________*
-------------------------------------------------------------------------------------------------
範例輸入3：
11
範例輸出3：
*____________________*
***________________***
*****____________*****
*******________*******
*********____*********
********************** 
*********____*********   
*******________*******   
*****____________*****
***________________***
*____________________*
-------------------------------------------------------------------------------------------------
範例輸入4：
4
範例輸出4：
Error
-------------------------------------------------------------------------------------------------
範例輸入5：
32
範例輸出5：
Error
"""


def myButterfly():
    n = int(input())
    if n % 2 == 0 or n < 4 or n > 30:
        print('Error')
    else:
        middleLine = int(n/2)
        for i in range(n):
            if i <= middleLine:
                eachSideStar = int(2*(i+1)-1)
                underLineNum = int(n * 2 - (2*(i+1)-1) * 2)
                printMyStar(eachSideStar, underLineNum)
            else:
                eachStar = int(2*((n-(i+1))+1)-1)
                underLine = int(n * 2 - (2*((n-(i+1))+1)-1) * 2)
                printMyStar(eachStar,underLine)

def printMyStar(star_num,underline_num):
    print(star_num * '*', end='')
    print(underline_num * '_', end='')
    print(star_num * '*', end='')
    print()


"""
23. 閏年判斷
閏年(Leap year)以下規則:
公元年分非4的倍數，為平年。
公元年分為4的倍數但非100的倍數，為閏年。
公元年分為100的倍數但非400的倍數，為平年。
公元年分為400的倍數為閏年。
現在給予N個年份( 1 <= N <= 10)
印出這些年份為閏年或平年，年份的範圍為公元1年到公元10000年
例如N = 5時：
輸入為：
5
1987
1988
1990
1991
1992
輸出為：
1987 is normal year.
1988 is leap year.
1990 is normal year.
1991 is normal year.
1992 is leap year.
-------------------------------------------------------------------------------------------------
輸入說明:
第一行輸入N個年份 (1 <= N <= 10)。
接下來N行，每行皆輸入年份Y (1 <= Y <= 10000)。
輸出說明:
依照輸入的N值，輸入N個年份，並且根據輸入的年份，判斷閏年或是平年。
------------------------------------------------------------------------------------------------
範例輸入 1:
2
1900
2000
範例輸出 1:
1900 is normal year.
2000 is leap year.
-------------------------------------------------------------------------------------------------
範例輸入 2:
3
1888
1901
2000
範例輸出 2:
1888 is leap year.
1901 is normal year.
2000 is leap year.
-------------------------------------------------------------------------------------------------
範例輸入 3:
9
1500
1600
1700
1800
1900
2000
2100
2020
2021
範例輸出 3:
1500 is normal year.
1600 is leap year.
1700 is normal year.
1800 is normal year.
1900 is normal year.
2000 is leap year.
2100 is normal year.
2020 is leap year.
2021 is normal year.
"""


def myYear():
    n = int(input())
    if n < 1 or n > 10:
        print('Error')
    else:
        yearList = []
        for i in range(n):
            y = int(input())
            yearList.append(y)
        for j in yearList:
            if j < 1 or j > 10000:
                print('Error')
            if j % 4 == 0:
                if j % 100 == 0:
                    if j % 400 == 0:
                        print("{} is leap year.".format(j))
                    else:
                        print("{} is normal year.".format(j))
                else:
                    print("{} is leap year.".format(j))
            else:
                print("{} is normal year.".format(j))

"""
24.
今天給予兩個正整數N (1 <= N <= 9) 與 D(0 <= D <= 4)
N代表 n*n的數字矩陣，D代表方向
方向分為以下五種方式實作：
D = 0，矩陣維持原樣
D = 1，矩陣向左旋轉90度
D = 2，矩陣向右旋轉90度
D = 3，矩陣上下翻轉
D = 4，矩陣左右翻轉
請使用迴圈並給予其中一種方向，印出 0 ~ n * n – 1的數字矩陣，數字之間請使用字串格式化 '%3d' 進行排版。
例如：
N = 5，D = 0，則輸出圖形如下
 0  1  2  3  4
 5  6  7  8  9
10 11 12 13 14 
15 16 17 18 19
20 21 22 23 24
-------------------------------------------------------------------------------------------------
N = 7， D = 1，則輸出圖形如下
6 13 20 27 34 41 48
5 12 19 26 33 40 47
4 11 18 25 32 39 46
3 10 17 24 31 38 45
2  9 16 23 30 37 44
1  8 15 22 29 36 43 
0  7 14 21 28 35 42 
------------------------------------------------------------------------------------------------
輸入說明：
第一行輸入正整數N，N代表n*n的數字矩陣 (1 <= N <= 9)
第二行輸入正整數D，D代表數字矩陣的方向 (0 <= D <= 4)
輸出說明：
根據大小以及選擇的方向印出n*n的數字矩陣，數字之間使用字串格式化 ’%3d’ 進行排版對齊。
-------------------------------------------------------------------------------------------------
範例輸入1：
5
1
範例輸出1：
4 9 14 19 24
3 8 13 18 23
2 7 12 17 22
1 6 11 16 21
0 5 10 15 20
-------------------------------------------------------------------------------------------------
範例輸入2：
3
2
範例輸出2：
6 3 0
7 4 1
8 5 2
-------------------------------------------------------------------------------------------------
範例輸入3：
7
0
範例輸出3：
 0  1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27 
28 29 30 31 32 33 34
35 36 37 38 39 40 41
42 43 44 45 46 47 48
-------------------------------------------------------------------------------------------------
範例輸入4：
9
3
範例輸出4：
72 73 74 75 76 77 78 79 80
63 64 65 66 67 68 69 70 71
54 55 56 57 58 59 60 61 62
45 46 47 48 49 50 51 52 53
36 37 38 39 40 41 42 43 44
27 28 29 30 31 32 33 34 35
18 19 20 21 22 23 24 25 26
 9 10 11 12 13 14 15 16 17
 0  1  2  3  4  5  6  7  8
-------------------------------------------------------------------------------------------------
範例輸入5：
8
4
範例輸出5：
 7  6  5  4  3  2  1  0
15 14 13 12 11 10  9  8
23 22 21 20 19 18 17 16
31 30 29 28 27 26 25 24
39 38 37 36 35 34 33 32
47 46 45 44 43 42 41 40
55 54 53 52 51 50 49 48
63 62 61 60 59 58 57 56
"""


def myRotationNum():
    n = int(input())
    d = int(input())
    # 先列出正常
    original = [[0] * n for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            original[i][j] = count
            count += 1
    if d == 0:
        for i in range(n):
            for j in range(n):
                print('%3d' % original[i][j],end='')
                if (j+1) % n == 0:
                    print()
    elif d == 1:
        # 向左旋轉90度
        for i in range(n):
            for j in range(n):
                print('%3d' % original[j][n-(i+1)],end='')
                if (j+1) % n == 0:
                    print()
    elif d == 2:
        # 向右旋轉90度
        for i in range(n):
            for j in range(n):
                print('%3d' % original[n-(j+1)][i],end='')
                if (j + 1) % n == 0:
                    print()
    elif d == 3:
        # 上下翻轉
        for i in range(n):
            for j in range(n):
                print('%3d' % original[n-(i+1)][j],end='')
                if (j + 1) % n == 0:
                    print()
    elif d == 4:
        # 矩陣左右翻轉
        for i in range(n):
            for j in range(n):
                print('%3d' % original[i][(n-1)-j],end='')
                if (j + 1) % n == 0:
                    print()

if __name__ == '__main__':
    # drawStarsAndNums(10)
    # myButterfly()
    myYear()
    # myRotationNum()