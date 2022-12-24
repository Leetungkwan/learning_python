

age = int(input('请输入你的年龄： '))
if age <= 0:
    print('还在娘胎')
elif 0 < age < 18:
    print(f'您的年龄是{age}, 童工，不合法')
elif age > 60:
    print(f'您的年龄是{age}, 退休')
else:
    print(f'您的年龄是{age}, 合法')
