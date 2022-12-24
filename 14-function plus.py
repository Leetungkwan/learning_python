import package as pg

# 学员数据
info = []


# 系统需要死循环，直至用户输入6才退出系统
while True:
# 1. 显示功能界⾯面
    pg.print_info()
# 2. 用户选择功能
    user_num = int(input('请选择您需要的功能序号：'))
# 3. 根据⽤用户选择，执行不同的功能
    if user_num == 1:
       # print('添加学员')
        pg.add_info()
    elif user_num == 2:
       # print('删除学员')
        pg.del_info()
    elif user_num == 3:
        # print('修改学员信息')
        pg.modify_info()
    elif user_num == 4:
        # print('查询学员信息')
        pg.search_info()
    elif user_num == 5:
        # print('显示所有学员信息')
        pg.print_all_info()
    elif user_num == 6:
        # print('退出系统')
        exit()
    else:
        print('输⼊入错误，请重新输⼊入!!!')