myStr = 'hello world and itcast and itheima and Python'

# find and
print(myStr.find('and'))  # 12
print(myStr.find('and', 15, 30))  # 23
print(myStr.find('ands'))  # -1


# index and
print(myStr.index('and'))  # 12
print(myStr.index('and', 15, 30))  # 23
# print(myStr.index('ands'))  # 报错

# count and
print(myStr.count('and'))  # 2
print(myStr.count('and', 15, 30))  # 1
print(myStr.count('ands'))  # 0


# rfind and  从右侧开始寻找
print(myStr.rfind('and'))  # 35
print(myStr.rfind('and', 15, 30))  # 23
print(myStr.rfind('ands'))  # -1
