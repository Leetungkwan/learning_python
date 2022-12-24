# def print_line():
#     print('-' * 20)
#
# def print_lines(num):
#     # i = 0
#     # while i < num:
#     #     print_line()
#     #     i += 1
#     for i in range(num):
#         print_line()
#
# print_lines(5)


# def sum_num(a, b, c):
#     return a + b + c
#
#
# def average_num(a, b, c, ):
#     length = len(sum_num.__code__.co_varnames)
#     sum_result = sum_num(a, b, c)
#     return sum_result/ length
#
#
# print(average_num(1, 2, 3))
# print(type(average_num(1,2,3)))


# a = 100
# def testA():
#     print(a)
# def testB():
#     # global 关键字声明a是全局变量量
#     global a
#     a = 200
#     print(a)
# testA()
# testB()
# print(a)


# 函数
# def fn1():
#     return 200
#
# print(fn1)
# print(fn1())
#
# # lambda表达式
# fn2 = lambda: 100
# print(fn2)
# print(fn2())

# fn1 = lambda a : a
# print(fn1(10))

# fn2 = lambda **kwargs : kwargs
# print(fn2(name='john', id=1))
#
# dict = {'name':'john', 'id':1}
# print(dict)


students = [
{'name': 'TOM', 'age': 20},
{'name': 'ROSE', 'age': 19},
{'name': 'Jack', 'age': 22}
]

students.sort(key=lambda x: x['name'])
print(students)

students.sort(key=lambda x: x['name'], reverse=True)
print(students)