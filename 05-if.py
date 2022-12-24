

# prepare datas age

age = float(input('请输入你的年龄： '))


if age >= float(18):
    print(f'您输入的年龄是{age}, 已经成年，可以上网')
else:
    print(f'您输入的年龄是{age}，未成年，不能上网')

print('系统关闭')
