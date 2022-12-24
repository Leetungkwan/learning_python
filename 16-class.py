# 父类
# class A():
#     def __init__(self):
#         self.num = 1
#
#     def info_print(self):
#         print(self.num)
#
#
# class B(A):
#     pass
#
#
# C = B()
#
# C.info_print()

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'


    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[学校煎饼果子配方]'


    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # super(School, self).__init__()
        # super(School, self).make_cake()

class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
        self.__money = 200000


    def __info_print(self):
        print('这是私有方法')


    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')


    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)


    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


    def make_old_cake(self):
        super(Prentice,self).__init__()
        super(Prentice, self).make_cake()


class Tusun(Prentice):
    pass


daqiu = Prentice()
print(daqiu.__money)
daqiu.make_cake()

# daqiu.make_master_cake()
#
# daqiu.make_school_cake()
#
# daqiu.make_cake()

xiaoqiu = Tusun()
xiaoqiu.make_cake()
xiaoqiu.make_school_cake()
# xiaoqiu.make_master_cake()


