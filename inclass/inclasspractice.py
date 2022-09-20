def printMessage(name='Alan', age=18):
    print('Hello:' + name)
    print('your age is :' + str(age))


# 直接執行
# if __name__ == '__main__':
#     name = input('your name:')
#     age = int(input('your age:'))
#     printMessage(name, 16)

# if __name__ == '__main__':
#     print('Direct main')
# else:
#     print('import __name__ is :' + __name__)

# list
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["abc", 34, True, 40, "male"]
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

