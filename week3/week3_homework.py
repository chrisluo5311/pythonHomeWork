"""
撲克牌
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
A~10 點數為 1~10，J, K, Q 為 0.5。
 X, Y 兩個人各發三張撲克牌，加總點數接近 10.5 則贏。
超過 10.5 爆掉分數為 0 。
 程式
輸入X, Y 兩個人各發的五張撲克牌。
輸出兩個人的點數，以及A贏或B贏或平手
"""
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
        print("x wins")
    elif x < y:
        print("y wins")
    else:
        print("Tie")

if __name__ == '__main__':
    x1, x2, x3 = '10', 'Q', 'A'
    y1, y2, y3 = '9', 'K', 'J'
    aPoint = getSum(x1, x2, x3)
    print("aPoint:" + str(aPoint))
    bPoint = getSum(y1, y2, y3)
    print("bPoint:" + str(bPoint))
    compare(aPoint, bPoint)
