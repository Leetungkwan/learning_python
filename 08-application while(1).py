"""
1、 产生一个星星
2、 产生一行五个星星
3、 产生五行的2
"""
j = 1
while j <= 9:
    # 一行*****
    i = 1
    while i <= j:
        print(f'{i} * {j} = {j * i} ', end='\t')
        i += 1
    print()  # 一行*****换行
    j += 1