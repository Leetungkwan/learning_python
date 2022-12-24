"""
1. 出拳
   玩家：手动输入
   电脑：1、固定；2、随机
2. 判断输赢
   1、玩家 win
   2、打和
   3、电脑 win
"""

import random

# 出拳
player = int(input('请出拳：0-石头；1-剪刀； 2-布：'))
computer = random.randint(0, 2)
print(computer)

# 判断输赢
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
# 平局
elif player == computer:
    print('平局')
else:
    print('电脑获胜')

