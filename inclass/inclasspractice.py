from datetime import date
from datetime import datetime
import math


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
    thislist2 = ["apple", "banana", "cherry"]
    thislist2[1:3] = ["watermelon"]
    print(thislist)
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
    oe()
