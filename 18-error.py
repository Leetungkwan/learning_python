import time

# try:
#     print(1)
# except Exception:
#     print('error!!!')
# else:
#     print('go')

# try:
#     f = open('test1.txt')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(3)
#             print(content)
#     except:
#         print('程序意外中止')
# except:
#     print('没有这个文件')

class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度
        self.min_len = min_len


    def  __str__(self):
        return f'你输入的密码长度{self.length},系统要求的最少长度{self.min_len}'


def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            error = ShortInputError(len(con), 3)
            print(error)
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')


main()




