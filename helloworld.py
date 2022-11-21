"""
comment in
multiple
lines
"""
# comment in one line

def isPrime(x):
    a = [n for n in range(2, x + 1) if all(n % m != 0 for m in range(2, n))]
    print(a)
# isPrime(10)

def fibo(n):
    xn = 0
    x1,x2 = 0,1
    for i in range(n+1):
        if i == 0:
            xn = x1
        elif i == 1:
            xn = x2
        else:
            xn = x1 + x2
            x1 = x2
            x2 = xn
    return xn
# print(fibo(6))

def fibo111(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibo111(n-1) + fibo111(n-2)

# print(fibo111(6))
def fibo2(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        records = fibo2(n-1)
        records.append(records[-1]+records[-2])
        return records

recordList = fibo2(6)
print(recordList)