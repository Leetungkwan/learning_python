# 显示功能界面
def print_info():
    print('请选择功能------------')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


 
# 功能1：添加学员
def add_info():
    '''添加学员的代码'''

    # 1.接收⽤用户输⼊入学员信息
    new_id = input('请输⼊入学号：')
    new_name = input('请输⼊入姓名：')
    new_tel = input('请输⼊入⼿手机号：')

    # 2.判断是否添加这个学员，如果学员姓名已经存在报错提示，如果行吗不存在添加数据
    global info

    # 2.1 不允许姓名重复，判断用户输入的姓名和列表里字典的name对应的值相等则提示
    for i in info:
        if new_name == i['name']:
            print('输入错误')
            return    # 退出当前函数，后面代码不执行

    # 2.2 如果输入的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {}

    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    # 列表追加字典
    info.append(info_dict)

    print(info)

def del_info():
    '''删除学员数据'''

    # 1.输入学员姓名
    del_name = input('学员姓名：')

    # 2.判断学员是否存在
    global info
    # 2.1 若不存在，则报错
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:    #循环正常结束之后执行，与for同一级别
        print('该用户不存在')

    print(info)

def modify_info():
    '''修改学员信息'''
    # 1.输入学员姓名

    modify_name = input('学员姓名：')

    # 2.判断学员是否存在，存在则修改（电话），不存在则报错

    # 2.1声明全局变量

    global info

    # 2.2判断
    for i in info:
        if modify_name == i['name']:
            modify_tel = input('请输入修改后的电话：')
            i['tel'] = modify_tel
            break
    else:
        print('该学员不存在')

    print(info)

def search_info():
    '''查询学员信息'''
    # 1.输入一个学员的姓名
    search_name = input('请输入学员姓名：')

    # 2.判断该学员是否存在，若存在即输出该学员信息，不存在则报错
    # 2.1声明全局变量
    global info

    # 2.2 进行判断
    for i in info:
        if search_name == i['name']:
            print(i)
            break
    else:
        print('该学员不存在')

    print(info)

def print_all_info():
    '''显示所有学员信息'''

    global info
    print(info)