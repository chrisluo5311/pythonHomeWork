"""
30. 密碼分數
給定多組密碼，最少3組，最多5組
請計算每一組密碼的分數，輸出最高及最低的兩組密碼及這兩組密碼的分數
每一組密碼的長度介於3~15之間 (含3與15)
計算密碼分數的規則如下：
1. N 個英文字母小寫加 N 分。
2. X 個英文字母大寫加 X*3 分。
3. Y 個數字加 Y*2 分。
4. M 個特殊符號 { ~!@#$%^&*<>_+=} 加 M*5 分。
5. 有五個以上的數字且任兩個數字在密碼中的位置不相鄰，
例如：「9a9a9a9a9」，加 15 分。
例如：
9a9a9a9a9
54321abc
~!@#
-1
輸出為：
9a9a9a9a9 29
54321abc 13
______________________________________________
輸入說明：
每一行為一組要計算分數的密碼M ( 3 <= len(M) <= 15 )，任兩組密碼的分數不會相同。
若輸入的密碼未達5組，輸入 -1 則停止輸入。
密碼最少3組，最多5組。
輸出說明：
第一行輸出分數最高的密碼，以及該組密碼的分數。
第二行輸出分數最低的密碼，以及該組密碼的分數。
密碼與該組密碼的分數間以空格區隔。
______________________________________________
範例輸入1：
12345
abc
ABC
-1
範例輸出1：
12345 10
abc 3
______________________________________________
範例輸入2：
HenryIsMe
!a@b#c$d
RichSayHello
1a2b3c
1!2@3$4%5^6*7
範例輸出2：
1!2@3$4%5^6*7 59
1a2b3c 9
______________________________________________
範例輸入3：
0a1
0a1a2a3a4a5
!a@d
-1
範例輸出3：
0a1a2a3a4a5 32
0a1 5
"""
import math
import sys


def scoreRule(pwdList):
    specStr = "~!@#$%^&*<>_+="
    ansList = []
    lowestN, biggestN = sys.maxsize, 0
    lowStr, biggestS = "", ""
    for i in pwdList:
        scoreSum, countNum = 0, 0
        flag = -1
        nextS = ""
        for j in range(len(i)):
            thisS = i[j]
            if j != (len(i) - 1):
                nextS = i[j + 1]
            else:
                nextS = ""
            if thisS.islower():
                scoreSum += 1
            elif thisS.isupper():
                scoreSum += 3
            elif thisS.isdigit():
                scoreSum += 2
                countNum += 1
                if nextS.isdigit():
                    flag = 1
            elif thisS in specStr:
                scoreSum += 5
        if countNum >= 5 and flag == -1:
            scoreSum += 15
        if scoreSum > biggestN:
            biggestN = scoreSum
            biggestS = i
        if scoreSum < lowestN:
            lowestN = scoreSum
            lowStr = i

    ansList.append(biggestS)
    ansList.append(biggestN)
    ansList.append(lowStr)
    ansList.append(lowestN)
    return ansList


def countPwd():
    pwdList = []
    while True:
        n = str(input())
        if n == "-1":
            break
        else:
            pwdList.append(n)
            if len(pwdList) == 5:
                break
    ansList = scoreRule(pwdList)
    for i in range(len(ansList)):
        print(ansList[i], end=' ')
        if i == 1:
            print()


"""
31. 病毒流行
COVID-20病毒流行，請分析並計算A城市病毒流行的狀況。
A城市某一天開始從邊境移入 people 位確診者 ( 100 <= people <= 2000 )。
每一位確診者會傳染給 infectPeople 個人 ( 1 <= infectPeople <= 10)。
確診者經過 recoveryDay 天後康復( 1 <= recoveryDay <= 10)，就不會再傳染給其他人 。
該城市中有保護力（打過疫苗且確診後康復者）的人口比例為 protectedRate ( 0.1 <= protectedRate <= 1)，而在分析期間，A城市打過疫苗+已確診康復者為固定人數。
已知計算每日新增確診公式為：(infectPeople/recoveryDay)*(1-protectedRate)
其結果需去掉小數並取整數，
並且打過疫苗與已確診康復者不會被傳染，其他人則會被傳染確診。
請輸出 periodＷeek 周中 ( 1 <= periodＷeek <= 10 )、每周平均確診人數、每周平均新增確診人數、每周平均康復人數。
最後再輸出預估第幾周能夠達成當周0位平均新增確診人數。
例如：
1000
1
7
0.75
5
輸出為：
(Week 1, 1112, 176, 0)
(Week 2, 185, 12, 176)
(Week 3, 21, 1, 12)
(Week 4, 1, 0, 1)
(Week 5, 0, 0, 0)
4
______________________________________________
輸入說：
第一行輸入一個整數 people ( 100 <= people <= 2000 )
第二行輸入一個整數 infectPeople ( 1 <= infectPeople <= 10)
第三行輸入一個整數 recoveryDay ( 1 <= recoveryDay <= 10)
第四行輸入一個小數 protectedRate ( 0.1 <= protectedRate <= 1 )
第五行輸入一個整數 periodWeek ( 1 <= periodWeek <= 10)
輸出說明：
第一行輸入第一周、第一周的每周平均確診人數、第一周的每周平均新增確診人數以及第一周每周平均康復人數，持續至 periodWeek 行 (1 <= periodWeek <= 10，輸出人數若遇小數須無條件進位至整數)
第 periodWeek+1 行，輸出預估在第幾周能夠達成當周0平均確診人數。
______________________________________________
範例輸入1：
100
2
5
0.7
6
範例輸出1：
(Week 1, 111, 26, 16)
(Week 2, 40, 6, 13)
(Week 3, 10, 1, 4)
(Week 4, 1, 0, 1)
(Week 5, 0, 0, 0)
(Week 6, 0, 0, 0)
4
______________________________________________
範例輸入2：
200
3
7
0.9
5
範例輸出2：
(Week 1, 226, 37, 0)
(Week 2, 44, 3, 37)
(Week 3, 4, 0, 3)
(Week 4, 0, 0, 0)
(Week 5, 0, 0, 0)
3
______________________________________________
範例輸入3：
2000
5
10
0.9
9
範例輸出3：
(Week 1, 2324, 383, 0)
(Week 2, 1944, 108, 331)
(Week 3, 800, 44, 134)
(Week 4, 340, 19, 55)
(Week 5, 145, 8, 28)
(Week 6, 58, 3, 12)
(Week 7, 21, 1, 5)
(Week 8, 4, 0, 2)
(Week 9, 0, 0, 0)
8
"""


def covid():
    people = int(input())
    infectPeople = int(input())
    recoveryDay = int(input())
    protectedRate = float(input())
    periodWeek = int(input())

    sumInfect = people
    dayIncrease = 0
    toRecoverList = [sumInfect]
    recoveredList = []
    avgTotal = sumInfect
    avgDayIncrease = [sumInfect]
    predictWeek = 0
    countDay = 0
    for i in range(periodWeek):
        for j in range(1, 8):
            countDay += 1
            if countDay == 1:
                dayIncrease = math.floor(sumInfect * (infectPeople / recoveryDay) * (1 - protectedRate))
                toRecoverList.append(dayIncrease)
                avgDayIncrease.append(dayIncrease)
            else:
                if countDay > recoveryDay:
                    reco = toRecoverList.pop(0)
                    recoveredList.append(reco)
                    sumInfect -= reco
                sumInfect += dayIncrease
                avgTotal += sumInfect
                dayIncrease = math.floor(sumInfect * (infectPeople / recoveryDay) * (1 - protectedRate))
                toRecoverList.append(dayIncrease)
                avgDayIncrease.append(dayIncrease)

        avgInfected = math.ceil(avgTotal/7)
        avgTotal = 0
        avg_increase = 0
        for m in range(7):
            avg_increase += avgDayIncrease.pop(0)
        avg_increase = math.ceil(avg_increase/7)
        avg_recover = 0
        avgLen = len(recoveredList)
        for n in range(avgLen):
            avg_recover += recoveredList.pop(0)
        avg_recover = math.ceil(avg_recover/7)
        print('(Week %d, %d, %d, %d)'%((i+1),avgInfected,avg_increase,avg_recover))
        if avg_increase == 0 and predictWeek == 0:
            predictWeek = i+1
    print(predictWeek)




"""
32. 成對檢查
給定 N個 ( 1 <= N <= 5 ) 字串，
每一個字串M (1 <= len(M) <= 20) 由括號與特殊符號組成
括號共有六種： {, }, [, ], (, ), <, >, ⊂, ⊃,【,】
特殊符號共有四種： +, -, *, /
檢查這字串M中的括號是否成對出現，
如果括號成對出現，代表通過檢查，輸出"Pass"
並個別計算各個特殊符號出現的次數，按照+ - * / 的順序輸出各個符號的出現次數，中間以空格分開。
如果括號沒有成對出現，代表未通過檢查，輸出"Fail"，並等待下一個字串輸入。
檢查的方式採用如下規則:
左括號為： {, [, (, <, ⊂, 【
右括號為： }, ], ), >, ⊃, 】
同欄的上方一個左括號及下方一個右括號為一組成對的括號，
上下一組，共有六種括號配對。
例如：
3
{[(+-*/)]}
[***--+/]
[+-*)
輸出為：
Pass
1 1 1 1
Pass
1 2 3 1
Fail
______________________________________________
輸入說明：
第一行輸入數字 N (1<=N<=5)
第二行到第N+1行，
每一行為一個要做括號成對檢查的字串M ( 1 <= len(M) <= 20)
輸出說明：
第一行輸出該組字串M是否通過括號對稱檢查。
檢查通過輸出 "Pass”，並且第二行按照+ - * /的順序輸出各個特殊符號的出現次數。
檢查失敗則輸出 "Fail”，不須輸出第二行及第三行，直接等待下一串字元輸入
輸出次數及行數以字串M的結果決定，輸出格式相同。
______________________________________________
範例輸入1：
3
(){}[]**--
{<(+-+-+)>}
【+】【-】【*】【/】
範例輸出1：
Pass
0 2 2 0
Pass
3 2 0 0
Pass
1 1 1 1
______________________________________________
範例輸入2：
3
{<+>[/][x](y)}
{<+>[/][x](y)
{<+>[/][x](y})
範例輸出2：
Pass
1 0 0 1
Fail
Fail
______________________________________________
範例輸入3：
4
([x+y]*{(a+b)*((a+c)*d)})
([x+y]*{(a+b)*[(a+c]*d)})
([x-y]/{(a+b)-((a+c)*d)})
{(h+{a+b)(x*y}*z)}
範例輸出3：
Pass
3 0 3 0
Fail
Pass
2 2 1 1
Fail
"""


def coupleCheck():
    l1 = {
        "{": "}",
        "[": "]",
        "(": ")",
        "<": ">",
        "⊂": "⊃",
        "【": "】"
    }
    l2 = {"}", "]", ")", ">", "⊃", "】"}
    n = int(input())
    checkList = []
    for i in range(n):
        s = str(input())
        checkList.append(s)
    for j in checkList:
        flag = 1
        spec = {
            "+": 0,
            "-": 0,
            "*": 0,
            "/": 0
        }
        stack1 = []
        for k in j:
            if k in spec:
                spec[k] += 1
            elif k in l1:
                stack1.append(l1.get(k))
            elif k in l2:
                if stack1[len(stack1) - 1] == k:
                    stack1.pop()
                else:
                    flag = -1
                    break
        if flag == -1 or len(stack1) > 0:
            print('Fail')
        else:
            print('Pass')
            for m in spec:
                print(spec[m], end=' ')
            print()


if __name__ == '__main__':
    # countPwd()
    # coupleCheck()
    covid()
