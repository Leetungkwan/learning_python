myStr = 'hello world and itcast and itheima and Python'

# replace() 把and换成he  replace函数有返回值，返回值是修改后的字符串
new_str = myStr.replace('and', 'he', 10)
print(new_str)
# 调用replace函数，不会修改原来字符串的数据

# split()  分割，返回一个列表，丢失分割字符
list1 = myStr.split('and', 2)
print(list1)

# join()  合并列表里面的字符，成为一个大字符串
myList = ['aa', 'bb', 'cc']
new_list = '...'.join(myList)
print(new_list)