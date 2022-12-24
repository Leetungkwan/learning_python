import random
import  functools

# glo_num = 0
#
#
# def testA():
#     global glo_num
#     glo_num = 100
#
#
# def testB():
#     print(glo_num)
#
#
# testA()
# testB()
# print(glo_num)


# def test1():
#     a = random.randint(1,10)
#     return a
#
#
# def test2(num):
#     print(num)
#
#
# result = test1()
# test2(result)

# def user_info(name, age, gender):
#     print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
#
# user_info('Rose', age=20, gender='女')
# user_info('ming', gender='男', age=20)

# def user_info(name, age, gender='男'):
#      print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
#
#
# user_info('ming', 20, gender='女')

# def user_info(*args):
#     length = len(args)
#     for i in range(length):
#         print(f'第{i}数据{args[i]}')
#
#
# user_info('Tom', 18, 'man')

# def user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}={value}')
#
# user_info(name='Tom', gender='man',id='110')
#

# def return_num():
#     return 100, 200
#
# num1, num2 = return_num()
# print(num1,num2)


# a = 1
# b = a
# print(b)
#
# print(id(a))
# print(id(b))

# aa = [10, 20]
# bb = aa
#
# aa.append(30)
# print(bb)
# print(id(aa))
# print(id(bb))
#
# def test1(a):
#     print(a)
#     print(id(a))
#     a = a * 2
#     print(a)
#     print(id(a))
#
#
# # int：计算前后id值不不同
# b = 100
# test1(b)
# # 列列表：计算前后id值相同
# c = [11, 22]
# test1(c)

list1 = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

result = map(func, list1)
print(list(result))

def func1(x, y):
    return x + y

result1 = functools.reduce(func1, list1)
print(result1)