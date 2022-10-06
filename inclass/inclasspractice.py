from datetime import date
from datetime import datetime
import math
import time


def printMessage(name='Alan', age=18):
    print('Hello:' + name)
    print('your age is :' + str(age))


# 直接執行
# if __name__ == '__main__':
#     name = input('your name:')
#     age = int(input('your age:'))
#     printMessage(name, 16)

# if __name__ == '__main__':
#     print('Direct main')
# else:
#     print('import __name__ is :' + __name__)


def printList():
    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))
    list1 = ["abc", 34, True, 40, "male"]
    mylist = ["apple", "banana", "cherry"]
    print(type(mylist))
    thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
    print(thislist)


def getListItem():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-1])
    print(thislist[-2])
    print(thislist[2:5])  # not included index 5
    print(thislist[-4:-1])  # not included index -1
    print(thislist[2:])
    print(thislist[:4])
    thislist5 = ["apple", "banana", "cherry"]
    if "apple" in thislist5:
        print("Yes, 'apple' is in the fruits list")


def changeList():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)
    thislist = ["apple", "banana", "cherry"]
    thislist[1:2] = ["blackcurrant", "watermelon"]
    print(thislist)
    thislist2 = ["apple", "banana", "cherry"]
    thislist2[1:3] = ["watermelon"]
    print(thislist2)
    thislist3 = ["apple", "banana", "cherry"]
    thislist3.insert(2, "watermelon")
    print(thislist3)


def get_area(length, width=4, height=5):
    return length * width * height


def countAge(num, birthyear):
    num = ((num * 2) + 5) * 50 + 1770
    finaleAge = num - birthyear
    return finaleAge


def integer_pick(num):
    num = int((num / 100) % 10)
    return num


def datetime_count(born):
    age = datetime.date.today() - born
    return age.days


def exception_handle():
    try:
        # 10/0
        raise (ZeroDivisionError("what?"))
    except ZeroDivisionError:
        print('ZeroDivisionError')
    else:
        print('else 區塊')
    finally:
        print('finally 區塊')


def raise_keyword():
    # x = -1
    # if x < 0:
    #     raise Exception("Sorry, no numbers below zero")
    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")


def read_file():
    f = open('E:/notepad筆記/北科/111_1北科大/程式設計/poem.txt', 'r')  # 開啟並讀取檔案 'r'代表讀取模式
    lines = f.readlines()  # 讀取檔案內容的每一行文字為陣列

    for line in lines:
        print(line, end='')  # 印出時結尾不印new line

    f.close()


def read_file02():
    # 用with來讀取並印出檔案內容。with結束時會自動關閉檔案，也就是不用另外寫f.close()。
    with open('E:/notepad筆記/北科/111_1北科大/程式設計/poem.txt', 'r') as f:
        content = f.read()  # 讀取檔案內容
    print(content, end='')  # 印出時結尾不印new line


"""
1.*args: 不定個數的參數加*
2.sort: reverse=True will sort the list descending. Default is reverse=False
"""


def getMaxNum(*a):
    print(type(a))
    tmp = list(a)
    print(tmp)
    tmp.sort(reverse=True)
    print(tmp[0])


"""
1. **kwargs: 如果想打包成字典(Dictionary)資料型態，則可以使用 ** 符號
"""


def getDict(**d):
    print(d)
    print(type(d))


"""
1. callback function
"""


def add(n1, n2, cb):
    cb(n1 + n2)


def handle1(result):
    print("結果是", result)


def handle2(result):
    print("Result of Add is", result)


def computeArea(cf, p):
    return cf(p)


def square(data):
    return data * data


def circle(data):
    return math.pi * data * data


def oe():
    num = int(input("input a num:"))
    if num == 100:
        print("special number!!!")
    elif num % 2 == 0:
        print("是偶數")
    else:
        print("是奇數")


def myScore():
    print("Hello~")
    score = int(input('輸入分數:'))
    if (score > 100) or (score < 0):
        print('成績輸入錯誤')
    elif score >= 60:
        print('恭喜你及格')
    else:
        print('不及格，要加油')


"""
若溫度(temperature )高於30而且沒有風wind=0，或濕度
(humidity)大於85，印出'開冷氣'
"""


def acOnAndOffv2(temp, wind, humidity):
    if (temp > 30 and wind == 0) or humidity > 85:
        print('開冷氣')


def findMiddle(a, b, c):
    x = list((a, b, c))
    x.sort()
    return x[1]


"""
A、B、C三本書價格及折扣表如下，一顧客欲購買A:ｘ本、
B:ｙ本、C:ｚ本（ｘ、ｙ、ｚ為使用者輸入），請計算需
花費多少錢？
  定價 1~10本 11~20本  21~30本  31本以上
A 380  原價   打9折    打8.5折   打8折
B 1200 原價   打9.5折  打8.5折   打8折
C 180  原價   打8.5折  打8 折    打7折
"""


def book_discount():
    x = int(input('A:'))
    y = int(input('B:'))
    z = int(input('C:'))
    A_discounts = [0.8, 0.85, 0.9, 1, 0]
    B_discounts = [0.8, 0.85, 0.95, 1, 0]
    C_discounts = [0.7, 0.8, 0.85, 1, 0]
    A_discount = getDiscount(x, A_discounts)
    B_discount = getDiscount(y, B_discounts)
    C_discount = getDiscount(z, C_discounts)
    cost = x * 380 * A_discount + y * 1200 * B_discount + z * 180 * C_discount
    print('The total cost is %d' % cost)


def getDiscount(x, discounts):
    discount = 0
    if x >= 31:
        discount = discounts[0]
    elif x >= 21:
        discount = discounts[1]
    elif x >= 11:
        discount = discounts[2]
    elif x >= 1:
        discount = discounts[3]
    else:
        discount = discounts[4]
    return discount


def scoreDivision():
    score = int(input('輸入分數:'))
    if score >= 90:
        print('得 A')
    elif score >= 80:
        print('得 B')
    elif score >= 70:
        print('得 C')
    elif score >= 60:
        print('得 D')
    else:
        print('不及格')


def print_ex():
    print("---RUNOOB EXAMPLE ： Loading 效果---")
    print("Loading", end="")
    for i in range(20):
        print(".", end='', flush=True)
        time.sleep(0.5)


def forOps():
    myString = "ATCgATAgcTCGaTCG"
    for index in myString:
        if index.isupper():
            print(index, end=" ")


def forOps2():
    i = 1
    myList = ["asm", "C", "python", "C++", "Java", "iOS", "Ruby", "perl", "delphi"]
    for index in myList:
        if index == "python":
            print(i, index)
        elif index == "Java":
            print(i, index)
        elif i % 3 != 0:
            print(i, index)
            i = i + 1
        else:
            i = i + 1


def getSum(num):
    sumVal = 0
    for i in range(num + 1):
        sumVal += i
    return sumVal


# 會考執行順序
def getSum3Times(m, n, step):
    sumVal = 0
    for i in range(m, n + 1, step):
        sumVal += i
    return sumVal, sumVal


def forOps3():
    i = 1
    myList = ["asm", "python", "C++", "Java", "iOS", "perl", "C#"]
    for index in myList:
        if (index == "Java"):
            print(i, index, end=', ')
        elif (index == "python"):
            print(i, index, end=', ')
        elif (i % 2 != 0):
            print(i, index, end=', ')
            i = i + 1
        else:
            i = i + 1


def getEq(x1, y1, x2, y2):
    m1 = y1 - y2
    m2 = x1 - x2
    b1 = x2 * y1 - x1 * y2
    b2 = x2 - x1
    return m1, m2, b1, b2


def equation(x1, y1, x2, y2):  # 1
    m = b = m1 = m2 = b1 = b2 = 0  # 2
    if (x1 == x2) and (y1 == y2):
        print('ERROR')  # 3
    if (x1 == x2):
        print('x=%d' % x1, end='')  # 4
    elif (y1 == y2):
        print('y=%d' % y1, end='')  # 5
    else:  # 6
        m1, m2, b1, b2 = getEq(x1, y1, x2, y2)  # 7
        print('y=', end='')  # 8
    if (m1 < 0) and (m2 < 0):  # 9
        m1 = -m1  # 10
        m2 = -m2  # 11
    if m1 == m2:
        print('', end='')  # 12
    elif m1 == (-m2):
        print('-', end='')  # ---(5) #13
    elif m1 % m2 == 0:  # 14
        m = m1 / m2;  # 15
        print('%d' % m, end='')  # 16
    else:
        print('%d/%d' % (m1, m2), end='')  # 17
    print('x', end='')  # 18
    if (b1 != 0):  # 19
        if (b1 * b2 > 0):
            print('+', end='')  # -(7) #20
    if (b1 % b2 == 0):
        print('%d' % (b1 / b2), end='')  # 21
    else:
        print('%d/%d' % (b1, b2), end='')  # 22
    print('')  # 23


def drawPyramid():
    for x in range(0, 10, 3):
        print(int(x / 3) * '#', end='')
        getNum(x)
        print('')


def getNum(x):
    for i in range(x, 10, 3):
        print(i, end='')


def test01():
    list = ['a', 'b', 'c', 'd', 'e', 'f']
    index = [3, 1, 2, 4, 5]
    i = 9
    for x in list:
        if i > len(list):
            print(list[index[7 - i]])
        i -= 1


"""
執行順序:
1, 2,3,4,5,6,4,5,6,4,5,6,4,5,4,5,6

"""


def forloop_str():  # 1
    myString = "ATCgATAgcTCGaTCG"  # 2
    s = 0  # 3
    for index in myString:  # 4
        if index.isupper():  # 5
            s += 1  # 6
    print(s)  # 7







################################################################################################
if __name__ == '__main__':
    # getListItem()
    # changeList()
    # print("area is: " + str(get_area(3)))
    # print(countAge(1, 1997))
    # print(integer_pick(67859))
    # datetime_count(x)
    # print(datetime.date.today())
    # exception_handle()
    # raise_keyword()
    # read_file()
    # read_file02()
    # getMaxNum(1, 2, 6, 9, 10, 55, 64, 1, 22, 3)
    # getDict(name='chris', id='12345', age='5')
    # test(handle)
    # add(3,4,handle1) # 結果是 7
    # add(5,6,handle2) # Result of Add is 11
    # print(computeArea(square, 5))
    # print(computeArea(circle, 5))
    # oe()
    # acOnAndOff(31, 0, 86)
    # myScore()
    # print(findMiddle(30, 10, 20))
    # print(findMiddle(30,20,10))
    # print(findMiddle(10,20,30))
    # print(findMiddle(10,30,20))
    # print(findMiddle(20,10,30))
    # book_discount()
    # print_ex()
    # forOps()
    # forOps2()
    # print(getSum(3))
    # forOps3()
    # 考順序
    # print(sumVal)
    # a = b = 0
    # a,b = getSum3Times(3, 12, 3)
    # print(a)
    # print(b)

    # equation(1,0,0,1) #24
    # equation(1,1,2,4) #25
    # equation(2,3,4,5) #26
    # equation(0,1,3,3)
    # drawPyramid()
    # test01()
    forloop_str()
