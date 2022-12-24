str1 = 'wait wait'
for i in str1:
    if i == 'a':
        break
    print(f'{i}', end='')

else :
    print()
    print('over')  # 分清楚break 和 continue 的区别

