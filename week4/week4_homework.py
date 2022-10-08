"""
013:
輸入m, n, a, b 四個整數，請計算m ~ n 之間等差為a的數列總和、等差為b的數列的乘積，
計算方式如下:
1. m ~ n 之間 等差為a的和:
m + (m+a) + (m+a*2) + (m+a*3) + ...
2. m ~ n 之間 等差為b的積:
m * (m+b) * (m+b*2) * (m+b*3) * ...
---------------------------------------------------
輸入說明 :
第一行，輸入整數 m
第二行，輸入整數 n
第三行，輸入整數 a
第四行，輸入整數 b
輸出說明 :
第一行輸出 m ~ n 之間 等差為a的數列的總和
第二行輸出 m ~ n 之間 等差為b的數列的乘積
---------------------------------------------------
範例輸入 1說明:
2
10
2
3
範例輸出 1說明:
30 (2~10之間等差為2的數列為: [2, 4, 6, 8, 10]，總和為30)
80 (2~10之間等差為3的數列為: [2, 5, 8]，乘積為80)
---------------------------------------------------
範例輸入 4說明:
-20
7
4
6
範例輸出 4說明:
-56 (-20~7之間等差為4的數列為: [-20, -16, -12, -8, -4, 0, 4]，總和為-56)
17920 (-20~7之間等差為4的數列為: [-20, -14, -8, -2, 4]，乘積為17920)
---------------------------------------------------
範例輸入1:
2
10
2
3
範例輸出 1:
30
80
—--------------------------------------------------
範例輸入2:
1
1
3
4
範例輸出 2:
1
1
—--------------------------------------------------
範例輸入3:
-100
100
2
3
範例輸出 3:
0
1933377063266786171556383835915513372677928926645598788472757611806350392456590325815705600000000000000000
—--------------------------------------------------
範例輸入4:
-20
7
4
6
範例輸出 4:
-56
17920
"""


def count_sequence():
    start = int(input())
    end = int(input())
    plus1 = int(input())
    plus2 = int(input())
    sumNum = 1
    multiSum = 1
    # 若首尾為1
    if start == 1 and end == 1:
        print("%d\n%d" % (sumNum, multiSum))
        return
    # 差和
    height1 = 0
    height2 = 0
    if start < 0 or end < 0:
        height1 = int((abs(start) + abs(end)) / plus1 + 1)
        height2 = int((abs(start) + abs(end)) / plus2)
    else:
        height1 = int((end - start) / plus1 + 1)
        height2 = int((end - start) / plus2)
    end1 = start + (height1 - 1) * plus1
    sumNum = ((start + end1) * height1) / 2
    print(int(sumNum))

    # 積和
    end2 = start + height2 * plus2
    for i in range(start, end2 + 1, plus2):
        multiSum *= i
    print(multiSum)


"""
14 -
輸入N個字串，請執行以下操作
1. 印出這N個字串中所有的小寫字母
(注意:若沒有字串中沒有小寫字母則輸出'No lowercase letters')
2. 輸出這N個字串中所有大寫字元的數量
3. 輸出這N個字串共有多少個字元 (含標點符號與空格)
4. 以空格分割這N個字串，將其中長度最長的單字輸出
---------------------------------------------------
輸入說明 :
第一行，輸入整數 N，代表接下來有N行輸入
第二 ~ N+1 行，輸入的字串，根據這N行執行操作1~4
輸出說明 :
第一行，輸出N個字串中所有的小寫字母
第二行，輸出N個字串中所有大寫字元的數量
第三行，輸出N個字串中所有字元的數量 (含標點符號、特殊字元與空格)
第四行，輸出以空格分割這N個字串後，其中長度最長的字串；若有多個長度最長的字串，輸出最早出現的字串
---------------------------------------------------
範例輸入 1說明:
2 (接下來輸入2行)
I have a pen I have an apple
Pen pineapple apple pen
範例輸出 1說明:
haveapenhaveanappleenpineappleapplepen (輸入的2個字串所有小寫字元)
3 (輸入的2個字串總共有2個大寫字元 (2個I))
51 (輸入的2個字串共有51個字元)
pineapple (以空格切分輸入的2個字串後，得到的所有字串為['I', 'have', 'a', 'pen', 'I', 'have', 'an', 'apple', 'Pen', 'pineapple', 'apple', 'pen']，其中最長的字串為'pineapple')
---------------------------------------------------
範例輸入 3說明:
2 (接下來輸入2行)
THE END OF THE WORLD
FINALE OF THE SHOW
範例輸出 3說明:
No lowercase letters (輸入的2個字串沒有任何小寫字元)
31 (輸入的2個字串共有31個大寫字元)
38 (輸入的2個字串共有38個字元)
FINALE (以空格切分輸入的2個字串後，得到的所有字串為['THE', 'END', 'OF', 'THE', 'WORLD', 'FINALE', 'OF', 'THE', 'SHOW']，其中最長的字串為'FINALE')
---------------------------------------------------
範例輸入 1:
2
I have a pen I have an apple
Pen pineapple apple pen
範例輸出 1:
haveapenhaveanappleenpineappleapplepen
3
51
pineapple
—--------------------------------------------------
範例輸入 2:
5
There's a growing trend among teenagers
A dead duck does not fly backward
I would be delighted
A song can make or ruin a person’s day
The pigs were insulted
範例輸出 2:
heresagrowingtrendamongteenagersdeadduckdoesnotflybackwardwouldbedelightedsongcanmakeorruinapersonsdayhepigswereinsulted
5
152
teenagers
—--------------------------------------------------
範例輸入 3:
2
THE END OF THE WORLD
FINALE OF THE SHOW
範例輸出 3:
No lowercase letters
31
38
FINALE
—--------------------------------------------------
範例輸入4:
2
*&^$(*#&%*#&$^&%*@^&
*&%#(*&#%(*&%Cry*$&%(&$%
範例輸出 4:
ry
1
44
*&%#(*&#%(*&%Cry*$&%(&$%
"""


def str_slicing():
    n = int(input())
    strList = []
    for i in range(n):
        str_input = str(input())
        strList.append(str_input)

    lower_str = ""
    upperCount = 0
    alphaCount = 0
    str_longest = ""
    for j in strList:
        lower_str += concat_lowercase(j)
        upperCount += count_uppercase(j)
        alphaCount += count_alpha(j)
        str_list = j.split(" ")
        x = count_longest(str_list)
        if len(x) > len(str_longest):
            str_longest = x

    # 小寫
    if lower_str != "":
        print(lower_str)
    else:
        print("No lowercase letters")
    # 大寫
    print(upperCount)
    # 字元數
    print(alphaCount)
    # 最常字
    print(str_longest)


def concat_lowercase(x=""):
    str_concat = ""
    for i in x:
        if i.islower():
            str_concat += i
    return str_concat


def count_uppercase(x=""):
    count = 0
    for i in x:
        if i.isupper():
            count += 1
    return count


def count_alpha(x=""):
    count = len(x)
    return count


def count_longest(x):
    longest_num = 0
    longest_str = ""
    for i in x:
        if len(i) > longest_num:
            longest_num = len(i)
            longest_str = i
    return longest_str


"""
15 - BMI

請設計計算BMI的程式，判斷A, B 兩個人，誰的BMI比較大

BMI值計算公式: BMI = 體重(公斤) / 身高^2(公尺^2)，例如：一個52公斤的人，身高是155公分，則BMI為 : 52(公斤)/1.55^2 ( 公尺^2 )= 21.6。
正常範圍BMI 為 18.5～24 (含18.5與24)。
當BMI太大，輸出 Hi {name}, Your BMI: {xxx} too HIGH.
當BMI太小，輸出 Hi {name}, Your BMI: {xxx} too LOW.
在正常範圍，輸出 Hi {name}, Your BMI: {xxx}.

若A比B重，輸出 {A}’s BMI is larger than {B}.
若B比A重，輸出 {B}’s BMI is larger than {A}.
★ 不會有雙方BMI相同的狀況

BMI輸出，四捨五入到小數點後第二位 (可用%.2f)。

---------------------------------------------------

輸入說明 :
第一行，輸入一字串，代表A的名字
第二行，輸入浮點數 w，代表A的體重
第三行，輸入浮點數 h，代表A的身高 (單位為公尺)
第四行，輸入一字串，代表B的名字
第五行，輸入浮點數 w，代表B的體重
第六行，輸入浮點數 h，代表B的身高 (單位為公尺)

輸出說明 :
第一行，依據A的BMI，輸出A的BMI屬於過重、過輕，還是正常
第二行，依據B的BMI，輸出B的BMI屬於過重、過輕，還是正常
第三行，輸出A跟B誰的BMI比較大
輸出格式請參考題目

—--------------------------------------------------

範例輸入 1說明:
Andrew (A的名字為 Andrew)
123.45 (A的體重為123.45 公斤)
1.71 (A的身高為1.71 公尺)
Kevin (B的名字為 Kevin)
81.77 (B的體重為81.77 公斤)
1.55 (B的身高為1.55 公尺)

範例輸出 1說明:
Hi Andrew, Your BMI: 42.22 too HIGH. (A的BMI為42.218，輸出成42.22，BMI過重)
Hi Kevin, Your BMI: 34.04 too HIGH. (B的BMI為34.035，輸出成34.04，BMI過重)
Andrew's BMI is larger than Kevin. (A的BMI比B大)

—--------------------------------------------------

範例輸入4說明:
Anthony (A的名字為 Anthony )
45 (A的體重為45 公斤)
1.68 (A的身高為1.68 公尺)
Mary (B的名字為 Mary )
100 (B的體重為100 公斤)
1.69 (B的身高為1.69 公尺)

範例輸出 4說明:
Hi Anthony, Your BMI: 15.94 too LOW. (A的BMI為15.943，輸出成15.94，BMI過輕)
Hi Mary, Your BMI: 35.01 too HIGH. (B的BMI為35.012，輸出成35.01，BMI過重)
Mary's BMI is larger than Anthony. (B的BMI比A大)

—--------------------------------------------------


範例輸入1:
Andrew
123.45
1.71
Kevin
81.77
1.55

範例輸出 1:
Hi Andrew, Your BMI: 42.22 too HIGH.
Hi Kevin, Your BMI: 34.04 too HIGH.
Andrew's BMI is larger than Kevin.

—--------------------------------------------------

範例輸入2:
John
77.66
1.23
Henry
40.7
1.6

範例輸出 2:
Hi John, Your BMI: 51.33 too HIGH.
Hi Henry, Your BMI: 15.90 too LOW.
John's BMI is larger than Henry.

—--------------------------------------------------

範例輸入3:
Larry
60
1.72
Bob
70
1.80

範例輸出 3:
Hi Larry, Your BMI: 20.28.
Hi Bob, Your BMI: 21.60.
Bob's BMI is larger than Larry.

—--------------------------------------------------

範例輸入4:
Anthony
45
1.68
Mary
100
1.69

範例輸出 4:
Hi Anthony, Your BMI: 15.94 too LOW.
Hi Mary, Your BMI: 35.01 too HIGH.
Mary's BMI is larger than Anthony.

—--------------------------------------------------

範例輸入5:
Jeff
30
1.32
Randy
50
1.85

範例輸出 5:
Hi Jeff, Your BMI: 17.22 too LOW.
Hi Randy, Your BMI: 14.61 too LOW.
Jeff's BMI is larger than Randy.
"""


def bmi_count_advanced():
    a_name = str(input())
    a_weight = float(input())
    a_height = float(input())
    a_bmi = a_weight / (a_height * a_height)

    b_name = str(input())
    b_weight = float(input())
    b_height = float(input())
    b_bmi = b_weight / (b_height * b_height)

    # check their range
    check_regular(a_bmi, a_name)
    check_regular(b_bmi, b_name)

    # compare
    if a_bmi > b_bmi:
        print("{}'s BMI is larger than {}.".format(a_name, b_name))
    else:
        print("{}'s BMI is larger than {}.".format(b_name, a_name))


def check_regular(bmi, name):
    if bmi > 24:
        print("Hi %s, Your BMI: %.2f too HIGH." % (name, bmi))
    elif bmi < 18.5:
        print("Hi %s, Your BMI: %.2f too LOW." % (name, bmi))
    else:
        print("Hi %s, Your BMI: %.2f." % (name, bmi))


"""
16 -
請使用迴圈 (while loop 或 for loop)
繪製三種不同的圖形
圖形請考範例測資
---------------------------------------------------
輸入說明 :
第一行，輸入整數 1 or 2 or 3，代表接下來要畫的圖形種類
第一種圖形為 三角形尖方面向右邊 (參考 範例輸出 1 or https://ppt.cc/fMFokx)
第二種圖形為 三角形尖方面向左邊 (參考 範例輸出 2 or https://ppt.cc/fhcJ8x)
第三種圖形為 菱形 (參考 範例輸出 3 or https://ppt.cc/fE35Nx)
第二行，輸入整數 N ，代表這個圖形有N行(僅接受奇數)
輸出說明 :
根據輸入，畫出對應的圖形
若整數N不是奇數，則改為輸出ERROR，並結束程式
此題不考慮第一行輸入1,2,3以外的情況
---------------------------------------------------
範例輸入1:
1
7
範例輸出 1:
*
**
***
****
***
**
*
—--------------------------------------------------
範例輸入2:
2
5
範例輸出 2:
..*
.**
***
.**
..*
—--------------------------------------------------
範例輸入3:
3
3
範例輸出 3:
.*.
***
.*.
—--------------------------------------------------
範例輸入4:
1
4
範例輸出 4:
ERROR
"""


def my_drawings():
    num1 = int(input())
    num2 = int(input())
    if num2 % 2 == 0:
        print("ERROR")
        return

    if num1 == 1:
        print1(num2)
    elif num1 == 2:
        print2(num2)
    else:
        print3(num2)


def print1(num):
    maxNum = int((num / 2) + 1)
    count_up = 1
    count_down = maxNum - 1
    for i in range(num):
        if count_up <= maxNum:
            print("*" * count_up)
            count_up += 1
        elif count_up > maxNum:
            print("*" * count_down)
            count_down -= 1


# 要印出.
def print2(num):
    maxNum = int((num / 2) + 1)
    count_up = 1
    count_down = maxNum - 1
    for i in range(num):
        if count_up <= maxNum:
            print("." * (maxNum - count_up) + "*" * count_up)
            count_up += 1
        elif count_up > maxNum:
            print("." * (maxNum - count_down) + "*" * count_down)
            count_down -= 1


def print3(num):
    maxNum = num
    count = 1
    count_down = maxNum - 2
    for i in range(num):
        if count <= maxNum:
            dotNum = int((maxNum - count) / 2)
            print("." * dotNum + "*" * count + "." * dotNum)
            count += 2
        elif count > maxNum:
            dotNum = int((maxNum - count_down) / 2)
            print("." * dotNum + "*" * count_down + "." * dotNum)
            count_down -= 2


if __name__ == '__main__':
    # count_sequence()
    # str_slicing()
    bmi_count_advanced()
    # my_drawings()
