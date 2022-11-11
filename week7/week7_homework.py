"""
A25.
請繪製兩個不同的圖形:
1. 井字號、星號、英文字母的複合圖形
2. 數字、星號的複合圖形
給予兩個正整數 N、M
N 代表要繪製的圖形種類，N的範圍為 (1 <= N <= 2)
M 代表要繪製的圖形高度，M的範圍有兩種情況
當 N = 1 時，代表繪製井字號、英文字母、星號的複合圖形，M的範圍為(2 <= M <= 29)
當 N = 2 時，代表繪製數字、星號的複合圖形，M的範圍為(1 <= M <= 9)
當 N 不為 1 或 2 時，輸出ERROR字串並結束程式
當N = 1時，輸出格式為：
第一層為 M - 1 個井字號、1 個星號、 M - 1個井字號
第二層為 M - 2 個井字號、1 個英文字母與 2 個星號、M - 2個井字號
第三層為 M - 3 個井字號、2 個英文字母與 3 個星號、M - 3個井字號
井字號、英文字母、星號的數量，依照規則以層數以此類推，直到 M 行結束。
除了第一層外，每層的英文字母以A、B、C作為循環。規則如下:
第二層的英文字母為A
第三層的英文字母為B
第四層的英文字母為C
第五層的英文字母回到A，以此類推循環，直到M行結束。
例如當N = 1, M = 5時 :
1
5
輸出圖形為：
####*####
###*A*###
##*B*B*##
#*C*C*C*#
*A*A*A*A*
當 N = 2 時，輸出格式為：
第一行為 數字 1 及 M * 2 個星號 及 數字 1 。
第二行為 數字 1 到 2 及 (M - 1)*2 個星號 及 數字 2 到 1。
第三行為 數字 1 到 3 及 (M - 2)*2 個星號 及 數字 3 到 1。
數字的範圍和星號的數量，依照規則以層數以此類推，直到M行結束。
例如當N = 2, M = 5 時:
2
5
輸出圖形為：
1**********1
12********21
123******321
1234****4321
12345**54321
請注意：
若M不在上述的範圍內，直接輸出ERROR並結束程式。
輸入說明：
第一行輸入一整數N
當N = 1時，代表要繪製井字號、英文字母、星號的複合圖形
當N = 2時，代表要繪製數字、星號的複合圖形
第二行輸入對應代表圖形的高度M
若N = 1時，M的範圍為1 <= M <= 9
若N = 2時，M的範圍為2 <= M <= 29
輸出說明:
若N = 1時，輸出依照題目規則，有M行高的井字號、英文字母、星號的複合圖形。
若M數值範圍不在2 <= M <= 29，輸出ERROR並結束程式，不必輸出圖形
若N = 2時，輸出依照題目規則，有M行高的數字、星號複合圖形。
若M的數值範圍不在1 <= M <= 9，則輸出ERROR並結束程式，不必輸出圖形。
當N不為1或2時，則輸出ERROR並且結束程式，不需等待輸入M
-------------------------------------------------------------------------------------------------
範例輸入1:
1
3
範例輸出1:
##*##
#*A*#
*B*B*
-------------------------------------------------------------------------------------------------
範例輸入2:
1
7
範例輸出2:
######*######
#####*A*#####
####*B*B*####
###*C*C*C*###
##*A*A*A*A*##
#*B*B*B*B*B*#
*C*C*C*C*C*C*
------------------------------------------------------------------------------------------------
範例輸入3:
1
30
範例輸出3:
ERROR
-------------------------------------------------------------------------------------------------
範例輸入4:
2
3
範例輸入4:
1******1
12****21
123**321
-------------------------------------------------------------------------------------------------
範例輸入5:
2
7
範例輸入5:
1**************1
12************21
123**********321
1234********4321
12345******54321
123456****654321
1234567**7654321
-------------------------------------------------------------------------------------------------
範例輸入6:
2
10
範例輸入6:
ERROR
-------------------------------------------------------------------------------------------------
範例輸入7:
3
範例輸入7:
ERROR
"""


def myMultiGraph():
    n = int(input())
    if n < 1 or n > 2:
        print('ERROR')
    else:
        m = int(input())
        if n == 1:
            if 1 < m < 30:
                for i in range(m):
                    print((m - (i + 1)) * '#', end='')
                    for j in range((i * 2) + 1):
                        if j % 2 == 0:
                            print('*', end='')
                        else:
                            engStr = (i + 1) % 3
                            if engStr == 2:
                                print("A", end='')
                            elif engStr == 0:
                                print("B", end='')
                            else:
                                print("C", end='')
                    print((m - (i + 1)) * '#', end='')
                    print()
            else:
                print('ERROR')
        elif n == 2:
            if 0 < m < 10:
                for i in range(1, m + 1):
                    for j in range(1, i + 1):
                        print(j, end='')
                    print(((m - (i - 1)) * 2) * '*', end='')
                    for k in range(i, 0, -1):
                        print(k, end='')
                    print()
            else:
                print('ERROR')


"""
26.
已知有一公式
S(K) = 1^1 + 2^2 + 3^3 + 4^4 + 5^5 + … + K^K
將 K 代入公式中，可以求出一個數字
將該數字由右往左看，可以產生一個有序數列
假設 K = 2，則S(2) = 1 + 4 = 5，數列為5
假設 K = 3，則S(3) = 1 + 4 + 27 = 32，數列為2,3
假設 K = 5，則S(5) = 1 + 4 + 27 + 256 + 3125 = 3143，數列為3,4,1,3
給定一正整數 N ( 1 <= N <= 10)，代表接下來會輸入 N 行測資
每一行輸入的正整數為 K ( 1 <= K <= 15)，K 代表要被計算的數字
輸入每一個 K 時，會輸出兩行結果：
1. S(K) 的值
2. S(K) 的數列
請注意：
1. 當 K 超出範圍時，需輸出 "ERROR" 字串並繼續執行程式，直到測資輸入完畢
2. 若數列的長度 > 1，數列中的每一個數之間需用逗號進行分隔
輸入說明：
第一行輸入正整數 N，N 代表測資個數 (1 <= N <= 10)
接下來 N 行，每行輸入正整數 K，K 代表要被計算的數字 (1 <= K <= 15)
輸出說明：
針對 N 個 K ，印出每一個S(K)的值以及其數列，並且分成兩行輸出。
若 K 超出範圍請輸出 "ERROR" 字串，並繼續執行程式直到測資輸入完畢。
-------------------------------------------------------------------
輸入範例1：
1
3
輸出範例1：
32
2,3
-------------------------------------------------------------------
輸入範例2：
3
10
7
2
輸出範例2：
10405071317
7,1,3,1,7,0,5,0,4,0,1
873612
2,1,6,3,7,8
5
5
-------------------------------------------------------------------
輸入範例3：
4
15
16
6
4
輸出範例3：
449317984130199828
8,2,8,9,9,1,0,3,1,4,8,9,7,1,3,9,4,4
ERROR
50069
9,6,0,0,5
288
8,8,2
-------------------------------------------------------------------
輸入範例4：
3
11
0
7
輸出範例4：
295716741928
8,2,9,1,4,7,6,1,7,5,9,2
ERROR
873612
2,1,6,3,7,8
"""


def myEquation():
    num = int(input())
    if 1 <= num <= 10:
        kList = []
        for i in range(num):
            k = int(input())
            if 1 <= k <= 15:
                kList.append(k)
            else:
                kList.append('ERROR')
        sumList = []
        for j in kList:
            if j != 'ERROR':
                sumNum = 0
                for k in range(1, j + 1):
                    multiSum = 1
                    for l in range(1, k + 1):
                        multiSum *= k
                    sumNum += multiSum
                sumList.append(sumNum)
            else:
                sumList.append(j)

        for k in sumList:
            if k != 'ERROR':
                seqNum = k
                seqList = []
                while seqNum != 0:
                    n = seqNum % 10
                    seqNum = int(seqNum // 10)
                    seqList.append(n)
                print(k)
                print(*seqList, sep=',')
            else:
                print(k)


"""
27.
參考以下演算法:
1. 輸入n
2. 印出n
3. 如果n = 1 則停止
4. 如果n為奇數，將 n 設為 3n+1
5. 否則 n須被除以2
6. 回到第二步驟
這個問題稱為3n+1 problem，使用以上的演算法，可以得到一個數列，這個數列的長度被稱為n的cycle-length。
例如 N = 10 時，代入演算法得出的數列順序為 [10, 5, 16, 8, 4, 2, 1]
cycle length 為 7。
題目要寫一個程式:
輸入兩個數字 n, m 兩個整數，(1 <= n <= 10000, n <= m <= 10000)
求出介於n, m之間 (包含n, m)的每一個數字使用演算法後所產生出的數列中，最大的 cycle length 為多少。
例如當輸入為
1
10
輸出則為:
20
(1~10之間，9 的數列為 [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]，cycle length 為 20)
---------------------------------------------------------------------
輸入說明:
第一行輸入n，n 的範圍 (1 <= n <= 10000)
第二行輸入m，m 的範圍 (n <= m <= 10000)
輸出說明:
對於輸入的n, m，輸出介於n , m之間(包含n, m)的每一個數字使用演算法後所產生出的數列中的最大cycle length。
當兩個數字皆輸入完畢，有超出範圍的情況，則輸出"ERROR"字串(不需輸出 cycle length)。
---------------------------------------------------------------------
範例輸入1:
1
100
範例輸出1:
119
---------------------------------------------------------------------
範例輸入2:
10
15
範例輸出2:
18
---------------------------------------------------------------------
範例輸入3:
3333
4567
範例輸出3:
238
---------------------------------------------------------------------
範例輸入4:
20000
4
範例輸出4:
ERROR
---------------------------------------------------------------------
範例輸入5:
0
10001
範例輸出5:
ERROR
-------------------------------------------------------------------
"""


def algo1(n):
    nList = [n]
    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n /= 2
        nList.append(n)
    return len(nList)


def myWeirdProblem():
    n = int(input())
    m = int(input())
    if n < 1 or n > 10000 or m < n or m > 10000:
        print('ERROR')
    else:
        lenList = []
        bigNum = 0
        for i in range(n, m + 1):
            lenList.append(algo1(i))
        for j in lenList:
            if j > bigNum:
                bigNum = j
        print(bigNum)


if __name__ == '__main__':
    # myMultiGraph()
    myEquation()
    # myWeirdProblem()