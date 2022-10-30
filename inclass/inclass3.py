def printSquare(n):
    for i in range(n * n, 0, -1):
        print('%3d' % i, end='')
        if i % n == 0:
            print()

def t(i, n):
    x1 = i // n
    y1 = i % n
    y2 = x1
    x2 = n - y1 - 1
    return x2 * n + y2

def printSquare1(n):
    i = 0
    while i < n * n:
        print('%3d ' % i, end='')
        i = i + 1
        if i % n == 0:
            print()


def printSquare2(n):
    i = 0
    while i < n * n:
        print('%3d ' % t(i, n), end='')
    i = i + 1
    if i % n == 0:
        print()


def printTriangle1(n):
    star = 0
    level = 1
    while level <= n:
        print('*', end='')
        star = star + 1
        if star >= level:
            star = 0
            level = level + 1
            print()


def printTriangle3(n):
    star = 1
    level = 1
    while level <= n:
        print('%2d' % star, end='')
        star = star - 1
        if star == 0:
            level = level + 1
            star = level
            print()

def gcd(x, y):
    while (x > 0) and (y > 0):
        if x > y:
            x = x % y
        else:
            y = y % x
    return x if x > y else y

def my_partial_fn(x):
    if x:
        y = 10
    return y



if __name__ == '__main__':
    # printSquare(5)
    # printSquare1(4)
    # printTriangle1(4)
    printTriangle3(5)
    # print(gcd(18, 24))
    # print(gcd(90, 36))
    # print(my_partial_fn(1))

