import os

# # 1.用户输入目标文件
# old_name = input("请输入你要备份的文件名:")
# print(old_name)
#
# # 2.1
# index = old_name.rfind('.')
# if index > 0:
#     postfix = old_name[index:]
# else:
#     print('乱来')
#
# new_name = old_name[:index] + '[备份]' + postfix
#
# # 3.1打开文件
# old_f = open(old_name, 'rb')
# new_f = open(new_name, 'wb')
#
# # 3.2将源文件写入备份文件
# while True:
#     con = old_f.read(1024)
#     if len(con) == 0:
#         break
#     new_f.write(con)
#
# # 3.3关闭文件
#
# old_f.close()
# new_f.close()

# 1.rename():重命名
# os.rename('test.txt', 'test1.txt')

# 2.remove（）：移除

# 3.mkdir()
# os.mkdir('aa')

# 4.getcwd():获取当前目录
print(os.getcwd())