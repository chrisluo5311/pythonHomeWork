"""
009.
蘋果、奇異果、鳳梨，三種水果價格及折扣表如下，且老闆為了回饋社會，決定再加碼，購買總顆數(三種水果加起來) 達30顆，總金額再打8.7折。
今一顧客欲購買，蘋果:ｘ顆、 奇異果:ｙ顆、鳳梨:ｚ顆（x、y、z 為使用者輸入），
請計算本次購買需花費多少錢？
(若計算出的最終結果有小數，則直接無條件捨去小數點後的數字；所有計算過程都使用小數，只有在輸出結果時使用整數輸出)
-------------------------------------------------------------------
------------| 定價 | 1~10顆 | 11~15顆 | 16~20顆 | 21顆以上 (含21顆) |
-------------------------------------------------------------------
| 蘋果-----| 30---| 原價----| 9.5折-----| 9折-------| 8折----|
-------------------------------------------------------------------
| 奇異果--| 70---| 原價----| 9折-------| 8.5折-----| 7.5折-|
-------------------------------------------------------------------
| 鳳梨-----| 40---| 原價----| 8.5折-----| 8折-------| 8折---|
-------------------------------------------------------------------
-------------------------------------------------------------------
輸入說明:
第一行，輸入購買 x 顆蘋果
第二行，輸入購買 y 顆奇異果
第三行，輸入購買 z 顆鳳梨
輸出說明:
請輸出最後花費的總金錢
-------------------------------------------------------------------
範例輸入 1說明:
10  (購買 10 顆蘋果)
10  (購買 10 顆奇異果)
10  (購買 10 顆鳳梨)
範例輸出 1說明:
1218
(10顆蘋果共300元，10個奇異果共700元，10個鳳梨共400元，共1400元
總共買了30顆水果，打8.7折，1400 * 0.87 = 1218)
-------------------------------------------------------------------
Example Input 1：
10
10
10
Example Output 1：
1218
-------------------------------------------------------------------
Example Input 2：
10
16
20
Example Output 2：
1646
-------------------------------------------------------------------
Example Input 3：
0
30
0
Example Output 3：
1370
-------------------------------------------------------------------
Example Input 4：
1
5
60
Example Output 4：
2001
-------------------------------------------------------------------
Example Input 5：
21
21
21
Example Output 5：
1982
-------------------------------------------------------------------
Example Input 6：
1
2
3
Example Output 6：
290
-------------------------------------------------------------------
Example Input 7：
15
15
15
Example Output 7：
1637
"""


def food_discount():
    # 蘋果:ｘ顆、 奇異果:ｙ顆、鳳梨:ｚ顆
    x = int(input())
    y = int(input())
    z = int(input())
    x_discount = [1, 0.95, 0.9, 0.8]
    y_discount = [1, 0.9, 0.85, 0.75]
    z_discount = [1, 0.85, 0.8, 0.8]
    x_dis = get_discount(x, x_discount)
    y_dis = get_discount(y, y_discount)
    z_dis = get_discount(z, z_discount)
    cost = x * 30 * x_dis + y * 70 * y_dis + z * 40 * z_dis
    if (x + y + z) >= 30:
        cost *= 0.87
    return int(cost)


def get_discount(amount, discounts):
    discount = 0
    if amount >= 21:
        discount = discounts[3]
    elif amount >= 16:
        discount = discounts[2]
    elif amount >= 11:
        discount = discounts[1]
    elif amount >= 1:
        discount = discounts[0]
    return discount


"""
010.
撲克牌
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
A~10 點數為 1~10，J, K, Q 為 0.5。
玩家A, B 兩個人，各發三張撲克牌，加總點數越接近 10.5 的贏；
如果總點數相同，則雙方平手 (Tie)
總點數超過 10.5 (不含10.5) ，爆掉且分數為 0。
-------------------------------------------------------------------
輸入說明: 
第一 ~ 三行，輸入 玩家 A 的三張撲克牌
第四 ~ 六行，輸入 玩家 B 的三張撲克牌
輸出說明: 
第一行輸出 玩家 A 的總點數
第二行輸出 玩家 B 的總點數
第三行，如果玩家A獲勝，輸出 A Win；如果玩家B獲勝，輸出 B Win；若雙方平手，輸出 Tie
-------------------------------------------------------------------
範例輸入 1 說明: 
A  (玩家A的 第一張 撲克牌為 A)
2  (玩家A的 第二張 撲克牌為 2)
3  (玩家A的 第三張 撲克牌為 3)
2  (玩家B的 第一張 撲克牌為 2)
3  (玩家B的 第一張 撲克牌為 3)
4  (玩家B的 第一張 撲克牌為 4)
範例輸出 1 說明: 
6  (玩家A的總點數為 1 + 2 + 3 = 6)
9  (玩家B的總點數為 2 + 3 + 4 = 9)
B Win  (9 > 6，玩家B獲勝，輸出B Win)
-------------------------------------------------------------------
Example Input 1：
A
2
3
2
3
4
Example Output：
6
9
B Win
-------------------------------------------------------------------
Example Input 2：
A
2
3
A
2
3
Example Output 2：
6
6
Tie
-------------------------------------------------------------------
Example Input 3：
2
3
5
4
A
2
Example Output 3：
10
7
A Win
-------------------------------------------------------------------
Example Input 4：
10
9
8
8
9
10
Example Output 4：
0
0
Tie
-------------------------------------------------------------------
Example Input 5：
2
3
6
2
3
5
Example Output 5：
0
10
B Win
"""


def poker_init():
    a_1 = input()
    a_2 = input()
    a_3 = input()
    b_1 = input()
    b_2 = input()
    b_3 = input()
    a_sumPoint = getSum(a_1, a_2, a_3)
    b_sumPoint = getSum(b_1, b_2, b_3)
    print(a_sumPoint)
    print(b_sumPoint)
    compare(a_sumPoint, b_sumPoint)


def cardTransfer(card):
    cardPoints = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 0.5, "Q": 0.5,
                  "K": 0.5}
    return cardPoints.get(card)


def getSum(x, y, z):
    a = cardTransfer(x)
    b = cardTransfer(y)
    c = cardTransfer(z)
    sumPoint = a + b + c
    if sumPoint > 10.5:
        return 0
    return sumPoint


def compare(x, y):
    if x > y:
        print("A Win")
    elif x < y:
        print("B Win")
    else:
        print("Tie")


"""
011.
檢查三門課程是否衝堂，
依序輸入課程編號(數字)、
上課小時數(1-3小時)、
上課時間(星期1-5, 第1-9節)
-------------------------------------------------------------------
輸入說明: 
輸入三門課程的資訊
每一門課程的資訊
第一行為課程編號
第二行為上課小時數 H
接下來有H行，
每一行為一個兩位數數字，十位數表示星期幾，個位數表示第幾節

輸出說明:
輸出兩個衝突的課程編號，以及在哪一天的哪一節衝突，參考下列格式
{課程1編號} and {課程2編號} conflict on {衝堂在哪天哪節}
先輸入的課程為課程1，後輸入的課程為課程2
-------------------------------------------------------------------
範例輸入 1說明
1001 (第一門課課程編號)
3 (3小時，每節課1小時)
11 (星期1 第1節課)
12 (星期1 第2節課)
13 (星期1 第3節課)
1002 (第二門課課程編號)
3  (3小時，每節課1小時)
21 (星期2 第1節課)
22 (星期2 第2節課)
23 (星期2 第3節課)
1003 (第三門課課程編號)
3  (3小時，每節課1小時)
31 (星期3 第1節課)
32 (星期3 第2節課)
13 (星期1 第3節課)
範例輸出 1說明 (兩課程編號衝突在哪幾節)
1001 and 1003 conflict on 13 (課程1001跟課程1003，在星期1第3節衝堂，因課程1001先輸入，所以課程1001放前面)
------------------------------------------------------------------
Example Input 1：
1001
3
11
12
13
1002
3
21
22
23
1003
3
31
32
13
Example Output 1：
1001 and 1003 conflict on 13
-------------------------------------------------------------------
Example Input 2：
1001
1
11
1002
3
21
22
11
1003
3
31
32
33
Example Output 2：
1001 and 1002 conflict on 11
-------------------------------------------------------------------
Example Input 3：
1001
2
11
12
1002
3
21
22
41
1003
3
22
32
33
Example Output 3：
1002 and 1003 conflict on 22
"""


def class_init():
    classTime = 0
    c1 = input()
    c1_hour = int(input())
    c1_list = []
    for x in range(c1_hour):
        classTime = input()
        c1_list.append(classTime)
    c2 = input()
    c2_hour = int(input())
    c2_list = []
    for y in range(c2_hour):
        classTime = input()
        c2_list.append(classTime)

    c3 = input()
    c3_hour = int(input())
    c3_list = []
    for z in range(c3_hour):
        classTime = input()
        c3_list.append(classTime)

    allList = []
    allList.extend(c1_list)
    allList.extend(c2_list)
    allList.extend(c3_list)
    duNum = check_duplicate(allList)
    dIndexList = []
    for i in allList:
        if i == duNum and not dIndexList:
            dIndexList.append(allList.index(i) + 1)
        elif i == duNum and dIndexList:
            dIndexList.append(allList.index(i, dIndexList[0]) + 1)

    conflict_class = []
    for j in dIndexList:
        if j <= c1_hour:
            conflict_class.append(c1)
        elif j <= c1_hour + c2_hour:
            conflict_class.append(c2)
        else:
            conflict_class.append(c3)
    print("{} and {} conflict on {}".format(conflict_class[0], conflict_class[1], duNum))


def check_duplicate(all_list):
    checkList = []
    for i in all_list:
        if i not in checkList:
            checkList.append(i)
        else:
            return i


"""
012.
今天好熱好熱，好想開冷氣
給你今天的溫度 (0 ~ 100)、濕度 (0 ~ 100)，有沒有起風 (0、1，0代表沒風，1代表有風)
請根據以下條件，幫忙決定一下今天要不要開冷氣，如果要開冷氣，請決定要設定幾度
1. 如果 溫度高於 50 (含50)，不論濕度、有無起風，一律開冷氣且設定18度
2. 如果 溫度低於 25 (不含25)，不論濕度、有無起風，一律不開冷氣
3. 如果 溫度高於 30 (含30) 而且沒有風，或濕度大於85(含85)，則開冷氣且設定為24度
4. 如果 溫度介於 25到29之間 (含25跟29) 且濕度介於60到84(含60跟84)且有起風，或溫度介於 25到29之間 (含25跟29) 且濕度小於60(不含60)且無起風，則開冷氣且設定為27度
5. 除此之外的狀況皆不開冷氣
★若條件重複，以條件標號數字較小者優先判斷
-------------------------------------------------------------------
輸入說明:
第一行，輸入溫度 (0 ~ 100，為一整數)
第二行，輸入濕度 (0 ~ 100，為一整數)
第三行，輸入有無起風 (0、1，0代表沒風，1代表有風)
輸出說明:
根據條件決定要不要開冷氣
如果要開冷氣，請輸出要設定的溫度
如果不開冷氣，請輸出 Today is cool
-------------------------------------------------------------------
範例輸入 1說明:
50   (溫度為 50)
20   (濕度為 20)
0     (沒有起風)
範例輸出 1說明:
18 (溫度高於50，符合條件1，開冷氣且設定為18度)
範例輸入 4說明:
25   (溫度為 25)
60   (濕度為 60)
1     (有起風)
範例輸出4說明:
27 (溫度介於25~29，濕度介於60~84，有起風，符合條件4，開冷氣且設定27度)
-------------------------------------------------------------------
Example Input 1：
50
20
0
Example Output 1：
18
-------------------------------------------------------------------
Example Input 2：
20
100
1
Example Output 2：
Today is cool
-------------------------------------------------------------------
Example Input 3：
25
85
1
Example Output 3：
24
-------------------------------------------------------------------
Example Input 4：
25
60
1
Example Output 4：
27
-------------------------------------------------------------------
Example Input 5：
29
50
0
Example Output 5：
27
-------------------------------------------------------------------
Example Input 6：
25
0
1
Example Output 6：
Today is cool
"""


def avOnAndOff():
    temp = int(input())
    moist = int(input())
    wind = int(input())
    output = -1
    if temp >= 50:
        output = 18
    elif temp < 25:
        output = -1
    elif (temp >= 30 and wind == 0) or (moist >= 85):
        output = 24
    elif (temp >= 25 and moist >= 60 and wind == 1) or (temp >= 25 and moist < 60 and wind == 0):
        output = 27

    if output > 0:
        print(output)
    else:
        print("Today is cool")


if __name__ == '__main__':
    # x1, x2, x3 = '10', 'Q', 'A'
    # y1, y2, y3 = '9', 'K', 'J'
    # aPoint = getSum(x1, x2, x3)
    # print("aPoint:" + str(aPoint))
    # bPoint = getSum(y1, y2, y3)
    # print("bPoint:" + str(bPoint))
    # compare(aPoint, bPoint)
    # print(food_discount())
    # poker_init()
    # class_init()
    avOnAndOff()
