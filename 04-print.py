age = 18
name = 'TOM'
weight = 75.5
student_id = 1
# 我的名字是TOM
print('我的名字是%s' % name)
# 我的学号是0001
print('我的学号是%03d' % student_id)
# 我的体重是75.50公⽄
print('我的体重是%.2f公⽄' % weight)
# 我的名字是TOM，今年18岁了
print('我的名字是%s,今年%d岁了' % (name, age))
print('我的名字是%s,今年%d岁了' % (name, age + 1))
print (f'我的名字是{name},今年{age}岁了')

print('hello', end='  ')
print('world')
print('hello world')