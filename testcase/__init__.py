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


if __name__ == '__main__':
    # permutation1('abc')
    permutationComprehension('abc')
