# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# fib(4)
# """
# 1-2-4-7 -1-2-4-7 -1-2-4-7 -1-2-4-5-7 -1-2-3-7 -7-1-2-4-5 -7-1-2-4-7 -1-2-4-5-7- 1-2-3-7 -7-7
# """
#
#
# s = "4"
# x = "5"
#
# # if x.isdigit():
# #     print(x)
#
# l1 = ['{', '[', '(',' <', '⊂', '【']
# l2 = {'}', ']', ')', '>', '⊃', '】'}
#
#
# ans = ['{','<','{','【','【','【','{']
# n = '{'
# if ans[len(ans)-1] == n:
#     ans.pop()
#     print(ans)


# if '}' in l2:
#     print('yes')

# nlist = [1,2,3,4,5,6,7]
# print(nlist.pop())


def checkPalindrome(wordPal, index):
    strlength = len(wordPal)
    if strlength == 2:
        return True
    if index > strlength / 2:
        return True

    flag = False
    if wordPal[index] is wordPal[strlength - 1 - index] and checkPalindrome(wordPal, index + 1):
        flag = True
    return flag


def permutation1(s):
    if len(s) == 1:
        return s
    else:
        r = []
        for i in range(len(s)):
            x = s[i]
            y = s[:i] + s[1 + i:]
            z = permutation1(y)
            for sub in z:
                r = r + [x + sub]
                print(r)
        return r


"""
小考必考
"""


def permutationComprehension(s):
    if len(s) == 1:
        return s
    else:
        r = []
        for i in range(len(s)):
            r += [s[i] + sub for sub in permutation1(s[:i] + s[1 + i:])]
            print(r)
        return r


def binarySearch(data, left, right, key):
    mid = (left + right) // 2
    if data[mid] == key:
        return mid
    if left == right:
        return -1
    if data[mid] > key:
        right = mid - 1
    else:
        left = mid + 1
    return binarySearch(data, left, right, key)

def FracMix(x):
    num, dem = x.split('/')
    i = int(int(num)/int(dem))
    dem = Fraction(int(num)%int(dem), int(dem))
    return str(i)+'('+str(dem) + ')'

def turnFour(n):
    ans = [0,0,0,0]
    for i in range(3,-1,-1):
        if n - (2 ** i) >= 0:
            n -= (2**i)
            ans[4-(i+1)] = 1
            continue
    print(*ans,sep='')

def convertTen(s):
    sumNum = 0
    for i in range(len(s),0,-1):
        print(s[i-1:i])
        if s[i-1:i] == '1':
            sumNum += 2**(len(s)-i)
    return sumNum

from fractions import Fraction
if __name__ == '__main__':
    # permutation1('abc')
    # permutationComprehension('abc')
    # print(int(2.5//1))
    # x = int(2.5//1)
    # y = 2.5%1
    # print(Fraction(2.5))
    # print(str(x)+"(",end='')
    # print(str(Fraction(0.5))+")")

    a1 = Fraction(1, 2) + Fraction(4, 2)
    # print(a1)
    fList = str(a1).split('/')
    # print(fList[0])
    # print(fList[1])
    # print(FracMix('-5/2'))
    n = '27/43)'
    # print(n[:len(n)-1])

    # print(601% abs(-115))

    s = '0010'
    # print(s[1:2])
    # print(s[2:3])

    # turnFour(4)

    # convertTen('00001010')

    ctList = ['A F G ','A E Z ']
    # x = len(min(ctList,key=len))
    # for i in ctList:
    #     if len(i) == x:
    #         print(i)

    newlist = [2,3,6,7]
    right = sorted([x for x in newlist if x % 2 == 0],reverse=True)
    # print(right)



    p1 = '99'
    p2 = '1'
    firstp = p1[:]

    # print(2 ** 11)

    cargoList = []
    tmpList = [1]
    cargoList.append(tmpList)
    print(cargoList)


