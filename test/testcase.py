# 測試format
def format_practice():
    x = int(float(input("測試數字:")))
    print("測試數字為:{}".format(x))
    # 隨堂小式
    a = "This is a book, that is a cat～"
    print(a[-3:8:-3])

def count_longest(x):
    longest_num = 0
    longest_str = ""
    for i in x:
        if len(i) > longest_num:
            longest_num = len(i)
            longest_str = i
    return longest_str

if __name__ == '__main__':
    # txt = "There's a growing trend among teenagers"
    # str_list = txt.split(" ")
    # longest_str = ""
    # for i in str_list:
    #     longest_str = count_longest(str_list)
    # print(longest_str)

    for i in range(7):
        print(i)






