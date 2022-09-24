"""
005.
計算BMI
輸入身高(公分) 體重(公斤) (皆使用小數)
BMI = 體重(公斤) / (身高*身高)(公尺)
結果須輸出到小數點第一位
print("%.1f" %bmi)
---------------------------------------------------
輸入說明：
第一行輸入身高 (公分)
第二行輸入體重 (公斤)
輸出說明：
輸出僅一行，為BMI的數值，結果輸出到小數點後第一位
---------------------------------------------------
Example Input 1:
172.2
60.7
Example Output 1:
20.5
---------------------------------------------------
Example Input 2:
165.1
70.4
Example Output 2:
25.8
---------------------------------------------------
Example Input 3:
189.2
100.0
Example Output 3:
27.9
---------------------------------------------------
Example Input 4:
173.4
56.7
Example Output 4:
18.9
"""


def count_bmi():
    height = float(input())
    weight = float(input())
    height /= 100
    bmi = weight / (height * height)
    print("%.1f" % bmi)


"""
006.
1. 輸入兩個英文句子 A, B，兩個字串 x, y
2. 將兩個英文句子A, B 串聯成 句子C
3. 將句子C其中的字串x 取代成 字串y，另其變成句子D
4. 輸出句子C, 句子D長度的加總
5. 把句子D 前三個字以及最後三個字組合成 句子E
6. 重複輸出三次句子E
---------------------------------------------------
輸入說明：
第一行，輸入英文句子 A
第二行，輸入英文句子 B
第三行，輸入字串 x
第四行，輸入字串 y
輸出說明：
第一行，輸出句子C, 句子D長度的加總
第二行，重複輸出三次句子E
---------------------------------------------------
範例輸入 1 說明:
This is a book (句子A)
That is a cat (句子 B)
is (字串 x)
was (字串 y)
句子C為This is a bookThat is a cat
句子D為Thwas was a bookThat was a cat
句子E為Thwcat
範例輸出 1 說明:
57 (句子C長度為27，句子D長度為30，總和為57)
ThwcatThwcatThwcat (句子E為Thwcat，重複三次為ThwcatThwcatThwcat)
---------------------------------------------------
Example Input 1:
This is a book
That is a cat
is
was
Example Output 1:
57
ThwcatThwcatThwcat
---------------------------------------------------
Example Input 2:
I have a pen
I have an apple
pineapple
watermelon
Example Output 2:
54
I hpleI hpleI hple
---------------------------------------------------
Example Input 3:
My name is Jeff
My name is Jeff
_
!!
Example Output 3:
60
My effMy effMy eff
"""


def paraphrase_sentence():
    a = str(input())
    b = str(input())
    x = str(input())
    y = str(input())
    c = a + b
    d = c.replace(x, y)
    sumLength = len(c) + len(d)
    print(sumLength)
    e = d[0:3] + d[-3:]
    print(e * 3)


"""
007.
輸入為一個英文句子以及一個單字，
請print出句子的長度，並且把句子以輸入的單字進行分割後輸出。
---------------------------------------------------
輸入說明：
第一行，一個英文句子
第二行，一個在第一行的英文句子中有出現的單字
輸出說明：
第一行輸出句子的長度
第二行輸出以單字進行分割後的句子
★請注意第二行輸出的句子的輸出格式是否正確
---------------------------------------------------
Example Input 1:
Those who turn back never reach the summit.
who
Example Output 1:
43
['Those ', ' turn back never reach the summit.']
---------------------------------------------------
Example Input 2:
Bravery never goes out of fashion.
never
Example Output 2:
34
['Bravery ', ' goes out of fashion.']
---------------------------------------------------
Example Input 3:
A man is not old as long as he is seeking something.
is
Example Output 3:
52
['A man ', ' not old as long as he ', ' seeking something.']
--------------------------------------------------
Example Input 4:
Do the right thing Do Things Right
Do
Example Output 4:
34
['', ' the right thing ', ' Things Right']
"""


def split_sentence():
    a = str(input())
    b = str(input())
    print(len(a))
    c = a.split(b)
    print(c)


"""
008.
輸入為一個人的全名加上一組生日，
將以上資訊依下列格式輸出，
{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.
---------------------------------------------------
輸入說明：
第一行，輸入一個人的全名，
順序為FirstName LastName
第二行，輸入他的生日，
生日年、月、日會以/隔開，格式為yyyy/mm/dd
輸出說明：
套用以下格式輸出
{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.
---------------------------------------------------
Example Input 1:
kobe Bryant
1978/08/23
Example Output 1:
kobe is born at year 1978 month 08 day 23 in Bryant family.
--------------------------------------------------
Example Input 2:
kevin love
1988/09/07
Example Output 2:
kevin is born at year 1988 month 09 day 07 in love family.
---------------------------------------------------
Example Input 3:
Stephen Curry
1988/03/14
Example Output 3:
Stephen is born at year 1988 month 03 day 14 in Curry family.
"""


def format_sentence():
    fullname = str(input())
    namelist = fullname.split(" ")
    firstname = namelist[0]
    lastname = namelist[1]
    birthday = str(input())
    birthlist = birthday.split("/")
    year = birthlist[0]
    month = birthlist[1]
    day = birthlist[2]
    print("{} is born at year {} month {} day {} in {} family.".format(firstname, year, month, day, lastname))


# week1 main
# if __name__ == '__main__':
    # count_bmi()
    # paraphrase_sentence()
    # split_sentence()
    # format_sentence()