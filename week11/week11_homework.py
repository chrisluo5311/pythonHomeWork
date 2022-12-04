"""
33. 分數四則運算
給定兩個分數A及B，分數皆以 分子/分母 或 整數(分子/分母) 的方式表示，
再給定一個運算符號 ( +, -, *, / ) 表示兩個分數的運算行為，
再輸入一個英文字母 y 或 n ，y代表還有下一筆四則運算，n則代表結束執行。
計算兩個分數的四則運算：加法、減法、乘法、除法，並輸出兩個分數經四則運算後的結果，
結果需轉換為最簡分數，且若為假分數，需換算成帶分數，若為整數則直接輸出整數，
輸出格式為 分子/分母 或 整數(分子/分母)。
例如：
1/2
4/2
+
y
1/2
4/2
-
y
1/2
4/2
*
y
1/2
4/2
/
n
輸出為：
2(1/2)
-1(1/2)
1
1/4
___________________________________________
輸入說明：
第一行輸入一個分數，代表要進行運算的分數 A。
第二行輸入另一個分數，代表要進行運算的分數 B。
第三行輸入 ( +, -, *, / ) 其中一種運算符號，代表用於分數 A 和分數 B 要進行的四則運算之加法、減法、乘法、除法的運算符號。
第四行輸入 y 表示繼續下一筆分數運算，輸入順序如上所述。輸入 n 則表示執行完本次運算後停止。
輸出說明：
若輸入分數分母為0，則輸出"ERROR"。
輸出分數 A 和 B進行四則運算後的結果，結果需為最簡分數，且若為假分數需換算成帶分數，輸出格式為 分子/分母 或 整數(分子/分母)。
_____________________________________________
範例輸入1：
-10/25
-111/23
+
y
-130/6
-40/14
+
y
10(27/43)
7(5/33)
-
n
範例輸出1：
-5(26/115)
-24(11/21)
3(676/1419)
______________________________________________
範例輸入2：
-35/54
3(63/88)
/
y
-7/10
35/50
+
n
範例輸出2：
-1540/8829
0
______________________________________________
範例輸入3：
6/28
63/40
*
y
33/71
1/6
*
y
-9/28
-4(5/21)
/
n
範例輸出3：
27/80
11/142
27/356
____________________________________________
範例輸入4：
5/0
11/20
+
y
-2/9
7/0
/
n
範例輸出4：
ERROR
ERROR
"""
from fractions import Fraction

def fracTurn(str1):
    num1, dem1 = str1.split('/')
    i = int(int(num1)/int(dem1))
    dem1 = Fraction(abs(int(num1))%int(dem1), int(dem1))
    return str(i)+'('+str(dem1) + ')'

def myMath():
    operationList = []
    while True:
        x1 = input()
        x2 = input()
        x3 = input()
        x4 = input()
        operationList.append(x1)
        operationList.append(x2)
        operationList.append(x3)
        if x4 == 'n':
            break
        else:
            continue

    while len(operationList) != 0:
        n1List = []
        n2List = []
        n1 = operationList.pop(0)
        if n1.count('(')!= 0:
            tmpList = n1.split('(')
            s2 = tmpList[1][:len(tmpList[1])-1]
            num1,dem1 = s2.split('/')
            sum1 = int(tmpList[0])*int(dem1)
            if sum1 < 0:
                n1List.append("-"+str(int(num1)+abs(sum1)))
            else:
                n1List.append(str(int(num1)+sum1))
            n1List.append(dem1)
        else:
            n1List = n1.split('/')
        if int(n1List[1]) == 0:
            print('ERROR')
            operationList.pop(0)
            operationList.pop(0)
            continue
        f1 = Fraction(int(n1List[0]),int(n1List[1]))
        #
        n2 = operationList.pop(0)
        if n2.count('(') != 0:
            tmpList = n2.split('(')
            s2 = tmpList[1][:len(tmpList[1]) - 1]
            num1, dem1 = s2.split('/')
            sum1 = int(tmpList[0]) * int(dem1)
            if sum1 < 0:
                n2List.append("-"+str(int(num1)+abs(sum1)))
            else:
                n2List.append(str(int(num1) + sum1))
            n2List.append(dem1)
        else:
            n2List = n2.split('/')
        if int(n2List[1]) == 0:
            print('ERROR')
            operationList.pop(0)
            continue
        f2 = Fraction(int(n2List[0]), int(n2List[1]))
        op = operationList.pop(0)
        ans = 0
        if op == '+':
            ans = f1 + f2
        elif op == '-':
            ans = f1 - f2
        elif op == '*':
            ans = f1 * f2
        elif op == '/':
            ans = f1/f2
        if ans.denominator != 1:
            num, dem = str(ans).split('/')
            if abs(int(num)) > abs(int(dem)):
                print(fracTurn(str(ans)))
            else:
                print(ans)
        elif ans.denominator == 1:
            print(ans)

"""
34.電路
模擬一個數位IC，內有回饋電路與紀錄器電路。
輸入M 是二進位 8 位元，輸出是二進位 4 位元。
輸入範圍從 00000000 到 11111111 (十進位 0~255)
數位IC內有一個回饋電路,回饋方式:
C(M) = M 當 M (十進位) 為 0 或 M 為 1 時
C(M) = C(M/2) 當 M (十進位) 為偶數
C(M) = C((M+1)/2) 當 M (十進位) 為奇數
請以二進位輸出回饋次數
並且以十進位輸出每次回饋的數值，中間以一個數字分隔
例如 M=00001010 (十進位 10),則電路回饋依序為十進位 5, 3, 2, 1。
C(10)= C(5)=C(3)=C(2)=C(1)=1，共回饋 4 次。
數位IC內有一個紀錄器R，會記錄回饋電路的回饋次數。
R(M) = [C(M) 的回饋次數]，例如 R(10) = 4，
則此數位IC以二進位輸出回饋次數為 0100。
當輸入為-1時，則結束執行。
例如：
00001010
-1
輸出為：
0100
5 3 2 1
--------------------------------------------------------------------------------------------------------------
輸入說明:
第一行輸入第一個測試案例資料(二進位 8 bit 位元)
第二行輸入第二個測試案例資料(二進位 8 bit 位元)
....
最後 -1 結束
輸出說明:
第一行輸出一個測試案例資料的結果(二進位 4 bit 位元)
第二行輸出該測試案例的電路回饋依序(十進位)，
若電路無任何回饋則輸出"No Feedback"。
--------------------------------------------------------------------------------------------------------------
輸入範例 1：
00001010
-1
輸出範例 1：
0100
5 3 2 1
--------------------------------------------------------------------------------------------------------------
輸入範例 2：
00000000
10010110
11111111
-1
輸出範例 2：
0000
No Feedback
1000
75 38 19 10 5 3 2 1
1000
128 64 32 16 8 4 2 1
--------------------------------------------------------------------------------------------------------------
輸入範例 3：
10101010
01010101
01100110
10010011
01110010
-1
輸出範例 3：
1000
85 43 22 11 6 3 2 1
0111
43 22 11 6 3 2 1
0111
51 26 13 7 4 2 1
1000
74 37 19 10 5 3 2 1
0111
57 29 15 8 4 2 1
"""

def turnFour(n):
    ans = [0,0,0,0]
    for i in range(3,-1,-1):
        if n - (2 ** i) >= 0:
            n -= (2**i)
            ans[4-(i+1)] = 1
            continue
    print(*ans,sep='')

# C(10)= C(5)=C(3)=C(2)=C(1)=1
def feedback(n):
    time = 0
    record = []
    if n == 0:
        return time,record
    while n != 1:
        if n % 2 == 0:
            n /= 2
            time += 1
            record.append(int(n))
        elif n % 2 != 0:
            n = (n+1)/2
            time += 1
            record.append(int(n))
    return time,record

# 00001010
def convertTen(s):
    sumNum = 0
    for i in range(len(s),0,-1):
        if s[i-1:i] == '1':
            sumNum += 2**(len(s)-i)
    return sumNum

def myElectric():
    electricList = []
    while True:
        n = input()
        if n == '-1':
            break
        electricList.append(n)

    for i in electricList:
        num = convertTen(i)
        f1,record = feedback(num)
        turnFour(f1)
        if len(record) == 0:
            print('No Feedback')
        else:
            print(*record,'')

"""
35. 物流公司
物流公司有一個貨物倉庫要進行配送，
倉庫中貨物編號為貨物重量(1~9 公斤) + 貨物名稱(A~Z)組成，貨物編號不重複，
例如兩個貨物編號為1A和2A，則為不重複之貨物編號；
若兩個貨物編號為1A和1A，則為重複之貨物編號，
配送的貨車載重限制為M公斤(1 <= M <= 10)，貨車必須滿載才會出發配送，
若單一貨物重量超出貨車載重限制，則無法配送。
請計算貨物倉庫的貨物需要運送幾趟才能將貨物全部配送完，
貨物挑選配送方式依照先輸入的貨物編號優先進行挑選配送。
輸出並排序每趟配送了哪些貨物編號的貨物名稱。
輸出貨物的排序方式 :
單趟內的貨物排序，由貨物名稱英文字母小至大排序，
所有趟數排序，依照單趟的貨物數量由小排到大，
若貨物數量相同，則依序比對單趟裡的貨物名稱，英文字母小的優先輸出。
例如：
4Q 3A 2D 3C 5R 2F 1G
5
輸出為：
4
R
A D
C F
G Q
以上方輸入為例:
第一次挑選配送的貨物為: 4Q + 1G
第二次為: 3A + 2D
第三次為: 3C + 2F
第四次為: 5R
輸出經過排序後應為:
R
A D
C F
G Q
___________________________________________
輸入說明：
第一行輸入倉庫內的所有貨物編號。
第二行輸入貨車限重 (1 <= M <= 10)。
輸出說明：
若輸入的載重限制超出限制範圍，輸出 "Input Error"。
若貨物編號重複，輸出 "Duplicated ID"。
若單一貨物重量超出貨車載重限制，輸出 "Load limit exceeded"。
若貨物未滿載導致無法配送，輸出"Cannot be delivered"。
若上述皆不符合，輸出方式為:
第一行輸出配送的總趟數。
第二行後輸出排序後的配送貨物名稱。
_____________________________________________
範例輸入1：
4Q 3A 2D 3C 5R 2F 1G
5
範例輸出1：
4
R
A D
C F
G Q
______________________________________________
範例輸入2：
4A 3B 2C 3D 5E 2F 1G
11
範例輸出2：
Input Error
______________________________________________
範例輸入3：
4A 3B 2C 3B 5D 2E 1F
2
範例輸出3：
Duplicated ID
______________________________________________
範例輸入4：
4A 3B 2C 3D 5E 2F 1G
4
範例輸出4：
Load limit exceeded
______________________________________________
範例輸入5：
4A 3B 5E 2F 1G 4F
5
範例輸出5：
Cannot be delivered
______________________________________________
範例輸入6：
1D 2D 3D 4D 4G 2F 4A 1H 9B 3Q 7Q 5E 3A 2Z
10
範例輸出6：
5
B H
Q Q
A E Z
A F G
D D D D
______________________________________________
範例輸入7：
4S 3T 2N 3A 5K 2E 1W 4Q 3O 2O 1K 2L 2M 4C 1S 1P 5O
5
範例輸出7：
9
K
O
A E
C P
K Q
N T
O O
S W
L M S
"""

def alphaOrder(ctList,preAns):
    newAns = []
    for x,y in preAns.items():
        tmp1 = {}
        sortNum = []
        xNum = ctList.get(x)
        sortNum.append(xNum)
        tmp1[xNum] = x
        if y != '':
            # 如果x是A、y是Z E
            for m in y:
                if m != ' ':
                    yNum = ctList.get(m)
                    sortNum.append(yNum)
                    tmp1[yNum] = m
            sortNum.sort()
            val = ''
            for m in range(1,len(sortNum)):
                val = val + tmp1.get(sortNum[m]) + ' '
            # A: E Z
            newAns.append(tmp1.get(sortNum[0]) + ' ' + val)
        else:
            if len(x) > 1:
                newAns.append(x[1:2])
            else:
                newAns.append(x)

    while len(newAns) != 0:
        tmp3 = []
        smallestLen = len(min(newAns, key=len))
        for m in newAns:
            if len(m) == smallestLen:
                tmp3.append(m)
                continue
        tmp3.sort()
        for k in tmp3:
            newAns.remove(k)
            print(k)

# 4A 3B 5E 2F 1G 4F ==> 5
# 3B 1G ==> 5
def countWeight(ctList,maxNum):
    ans = {}
    flag = 0
    while len(ctList) != 0:
        ct1 = ctList.pop(0)
        if len(ctList) == 0:
            w1 = int(ct1[0:1])
            if w1 == maxNum:
                name1 = ct1[1:2]
                if name1 in ans:
                    ans[ct1] = ''
                else:
                    ans[name1] = ''
                break
            else:
                print('Cannot be delivered')
                flag = -1
                break
        sumWeigh = int(ct1[0:1])
        name1 = ct1[1:2]
        preAnsList = []
        if sumWeigh == maxNum:
            ans[name1] = ''
            continue
        for i in ctList:
            wi = int(i[0:1])
            sumWeigh += wi
            if sumWeigh == maxNum:
                if len(preAnsList) == 0:
                    ans[name1] = i[1:2]
                else:
                    val = ''
                    for j in preAnsList:
                        val = val + j[1:2] + ' '
                        ctList.remove(j)
                    ans[name1] = val + ' ' + i[1:2]
                ctList.remove(i)
                break
            elif sumWeigh < maxNum:
                preAnsList.append(i)
            elif sumWeigh > maxNum:
                sumWeigh -= wi
                continue
        if sumWeigh == int(ct1[0:1]) or sumWeigh < maxNum:
            flag = -1
            print('Cannot be delivered')
            break

    if flag == -1:
        return {}, 0
    else:
        return ans, len(ans.keys())


def myContainer():
    ctList = {
        'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
        'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,
        'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26
    }
    c1 = input()
    maxNum = int(input())
    c1List = c1.split(' ')
    for i in c1List:
        if c1List.count(i) > 1:
            print('Duplicated ID')
            return
    for j in c1List:
        n = int(j[0:1])
        if n > maxNum:
            print('Load limit exceeded')
            return
    if maxNum < 1 or maxNum > 10:
        print('Input Error')
        return

    preAns,times = countWeight(c1List,maxNum)
    if len(preAns) == 0 and times == 0:
        return
    print(times)
    alphaOrder(ctList, preAns)


if __name__ == '__main__':
    # myMath()
    # myElectric()
    myContainer()
