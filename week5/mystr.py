def str_slicing(n,str1,str2):
    strList = [str1, str2]

    lower_str = ""
    upperCount = 0
    alphaCount = 0
    str_longest = ""
    for j in strList:
        lower_str += concat_lowercase(j)
        upperCount += count_uppercase(j)
        alphaCount += count_alpha(j)
        str_list = j.split(" ")
        str_longest = find_longest(str_list,str_longest)


    # 小寫 大寫 字元數 最長字
    if lower_str != "":
        return lower_str,upperCount,alphaCount,str_longest
    else:
        return "No lowercase letters",upperCount,alphaCount,str_longest


def concat_lowercase(x=""):
    str_concat = ""
    for i in x:
        if i.islower():
            str_concat += i
    return str_concat


def count_uppercase(x=""):
    count = 0
    for i in x:
        if i.isupper():
            count += 1
    return count


def count_alpha(x=""):
    count = len(x)
    return count


def find_longest(x,str_longest):
    longest_num = 0
    longest_str = ""
    for i in x:
        if len(i) > longest_num:
            longest_num = len(i)
            longest_str = i

    if len(longest_str) > len(str_longest):
        return longest_str
    else:
        return str_longest
