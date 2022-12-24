from student import  *

class StudentManager(object):
    def __init__(self):
        # 存储学员信息
        self.student_list = []


    # 1.程序入口函数
    def run(self):
        # 1.1加载文件的学员数据
        self.load_student()
        while True:
            # 1.2显示功能菜单
            self.show_menu()
            # 1.3用户输入目标功能序号
            menu_num = int(input('请输入需要的功能序号: '))

            # 1.4 根据用户输入的序号执行不同功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存所有学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break


    # 2.系统功能函数
    # 2.1显示功能菜单
    @staticmethod
    def show_menu():
        print('请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    # 2.2 添加学员
    def add_student(self):
        name = input('请输⼊入您的姓名：')
        gender = input('请输⼊入您的性别：')
        tel = input('请输⼊入您的⼿手机号：')
        # 2. 创建学员对象：先导⼊入学员模块，再创建对象
        student = Student(name, gender, tel)
        # 3. 将该学员对象添加到列列表
        self.student_list.append(student)
        # 打印信息
        print(self.student_list)
        print(student)


    # 2.3 删除学员
    def del_student(self):
        # 1.输入要删除的学员姓名
        del_name = input('请输入你要删除学员的姓名：')

        # 2.遍历学员，判断删除
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print('没有此学员')

        print(self.student_list)

    # 2.4 修改学员信息
    def modify_student(self):
        # 1.输入需要修改的学员姓名
        modify_name = input('请输入需要修改的学员姓名：')

        for i in self.student_list:
             if i.name == modify_name:
                i.tel = int(input('请输入修改后的电话号码：'))
                break

        else:
            print('没有此学员')


    # 2.5 查询学员信息
    def search_student(self):
        # 1.输入要查询的学员姓名
        search_name = input('请输入你要查询学员的姓名：')

        # 2.遍历列表，判断
        for i in self.student_list:
            if i.name == search_name:
                print(f'该学员姓名为{i.name}, 该学员性别为{i.gender}, 该学员电话号码为{i.tel}')
                # print(i)
                break


    # 2.6 显示所有学员信息
    def show_student(self):
        for i in self.student_list:
            print(f'学员姓名为{i.name}, 该学员性别为{i.gender}, 该学员电话号码为{i.tel}')

    # 2.7 保存学员信息
    def save_student(self):
        # 1. 打开⽂文件
        f = open('student.data', 'w')

        # 2. ⽂文件写⼊入学员数据
        # 注意1：⽂文件写⼊入的数据不不能是学员对象的内存地址，需要把学员数据转换成列列表字典数据再做存储

        new_list = [i.__dict__ for i in self.student_list]

        print(new_list)
        # 注意2：⽂文件内数据要求为字符串串类型，故需要先转换数据类型为字符串串才能⽂文件写⼊入数据
        f.write(str(new_list))
        # 3. 关闭文件
        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        # 1.尝试以只读方式打开文件，如若没有就创建
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')

        # 2.文件里的数据为字符串类型，需要转换数据
        else:
            data = f.read()
            new_list = eval(data)
            for i in new_list:
                self.student_list.append(Student(i['name'], i['gender'], i['tel']))

        finally:
            f.close()
