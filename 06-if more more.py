"""
1. 是否能上车
2. 上车：是否能坐下；不上车：滚
"""
# 准备要做判断的数据，钱和空座
# 判断是否有钱
# 判断是否能坐下：有空位

money = int(input('请输入你的金钱数额：'))

seat = 1


if money >= 2:
    print('上车')
    if seat == 1:
        print('请坐下')
    else:
        print('站着吧，你')
else:
    print('滚')


