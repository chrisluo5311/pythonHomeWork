"""
15
*fedcba987654321
**edcba987654321
***dcba987654321
****cba987654321
*****ba987654321
******a987654321
*******987654321
********87654321
*********7654321
**********654321
***********54321
************4321
*************321
**************21
***************1
"""
import string
def myPrint(n):
    for i in range(n):
        print((i+1)*"*",end='')
        if n < 9:
            for j in range(n-i,0,-1):
                print(j,end='')
        else:
            x = (n+1) - (i+1)
            if x > 9:
                x = x - 9
                for k in list(string.ascii_lowercase)[-(26-(x-1))::-1]:
                    print(k,end='')
                for m in range(9,0,-1):
                    print(m,end='')
            else:
                for o in range(x,0,-1):
                    print(o,end='')
        print()


if __name__ == '__main__':
    # myPrint(15)
    myPrint(5)
