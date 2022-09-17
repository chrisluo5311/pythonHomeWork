"""
題目001 -
某一學生修國文Chinese、計算機概論CS、計算機程式設計PD三科，使用者輸入名字(string)、學號(int)、三科成績(int)。
請輸出學生名字、學號，並計算其平均成績與總分。
輸入說明 :
第一行，輸入學生名字
第二行，輸入學生學號
第三行，輸入學生國文成績
第四行，輸入學生計算機概論成績
第五行，輸入學生計算機程式設計成績
輸出說明 :
第一行輸出 Name:學生名字
第二行輸出 ID:學生學號
第三行輸出 Average:學生三科成績之平均 (保留整數即可)
第四行輸出 Total:學生三科成績之總分
---------------------------------------------------
Example Input 1:
Tom
905067
100
100
100
Example Output 1:
Name:Tom
ID:905067
Average:100
Total:300
-------------------------
Example Input 2:
Ray
106590035
99
90
82
Example Output 2:
Name:Ray
ID:106590035
Average:90
Total:271
-------------------------
Example Input3:
David
42015632
0
0
0
Example Output 3:
Name:David
ID:42015632
Average:0
Total:0
"""
from math import sqrt


def export_student():
    # 科目數量固定3
    subject_count = int(3)
    student_name = input("輸入學生名字:")
    student_id = input("輸入學生學號:")
    student_ch_grade = int(float(input("輸入學生國文成績:")))
    student_ca_grade = int(float(input("輸入學生計算機概論成績:")))
    student_cp_grade = int(float(input("輸入學生計算機程式設計成績:")))
    sum_grade = student_ch_grade + student_ca_grade + student_cp_grade
    average_grade = int(sum_grade / subject_count)
    print("Name:" + student_name)
    print("ID:" + student_id)
    print("Average:{}".format(average_grade))
    print("Total:{}".format(sum_grade))


"""
題目 002 -
一元二次方程式，ax^2 + bx + c = 0，輸入a, b, c, 求 方程式的兩個實根。
-----------------------------
輸入說明
第一個數(int) a
第二個數(int) b
第三個數(int) c
-----------------------------
輸出說明
第一個實根 x1 = ((-b)+sqrt(b*b-4*a*c))/(2*a)
第二個實根 x2 = ((-b)-sqrt(b*b-4*a*c))/(2*a)
x1, x2 輸出到小數點第一位
print("%.1f" %x1)
-----------------------------
Example Input 1
1
-2
1
Example Output 1
1.0
1.0
-------------------
Example Input 2
7
0
0
Example Output 2
0.0
0.0
-------------------
Example Input 3
1
0
-1
Example Output 3
1.0
-1.0
-------------------
Example Input 4
41
17
-27
Example Output 4
0.6
-1.0
-------------------
Example Input 5
-100
100
100
Example Output 5
-0.6
1.6
"""


def quadratic_equation():
    a = int(float(input("第一個數a:")))
    b = int(float(input("第二個數b:")))
    c = int(float(input("第三個數c:")))
    x1 = ((-b) + sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = ((-b) - sqrt(b * b - 4 * a * c)) / (2 * a)
    print("%.1f" % x1)
    print("%.1f" % x2)


"""
題目 003 -
分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。
結果須輸出到小數點第二位
print("%.2f" %ans)
---------------------------------------------------
輸入說明
第一行，輸入數字num1
第二行，輸入數字num2
---------------------------------------------------
輸出說明
第一行輸出Sum:num1+num2
第二行輸出Difference:num1-num2
第三行輸出Product:num1*num2
第四行輸出Quotient:num1/num2
加減乘除的結果，輸出到小數點後第二位
print("%.2f" %ans)
---------------------------------------------------
Example Input 1:
25
2
Example Output 1:
Sum:27.00
Difference:23.00
Product:50.00
Quotient:12.50
--------------------------------
Example Input 2:
-1
6
Example Output 2:
Sum:5.00
Difference:-7.00
Product:-6.00
Quotient:-0.17
--------------------------------
Example Input 3:
0
9
Example Output 3:
Sum:9.00
Difference:-9.00
Product:0.00
Quotient:0.00
"""


def basic_math():
    num1 = int(float(input("輸入數字num1:")))
    num2 = int(float(input("輸入數字num2:")))
    ans_sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    print("Sum:%.2f" % ans_sum)
    print("Difference:%.2f" % difference)
    print("Product:%.2f" % product)
    print("Quotient:%.2f" % quotient)


"""
題目 004 -
A、B、C三本書價格如下，一顧客欲購買A:ｘ本、B:ｙ本、C:ｚ本（ｘ、ｙ、ｚ為使用者輸入），請計算需花費多少錢？
定價
A 380
B 1200
C 180
---------------------
Example input:
8
9
5
Example output:
14740
---------------------
Example input:
0
0
0
Example output:
0
---------------------
Example input:
1
0
4
Example output:
1100
"""


def book_sum():
    # a、b、c定價
    a_price = int(380)
    b_price = int(1200)
    c_price = int(180)
    x = int(float(input("a本數x:")))
    y = int(float(input("b本數y:")))
    z = int(float(input("c本數z:")))
    a_sum = x * a_price
    b_sum = y * b_price
    c_sum = z * c_price
    total_price = a_sum + b_sum + c_sum
    print(total_price)
