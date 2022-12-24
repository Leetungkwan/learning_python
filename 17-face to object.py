# 需求：警务人员与警犬一起工作，警犬分两种。

# # 1.父类
# class Dog(object):
#     def work(self):
#         print('指哪打哪')
#
# # 2.子类
# class ArmyDog(Dog):
#     def work(self):
#         print('追击敌人')
#
#
# class DrugDog(Dog):
#     def work(self):
#         print('追查毒品')
#
#
# class Person(object):
#     def work_with_dog(self,dog):
#         dog.work()
#
#
# # 创建对象
# ad = ArmyDog()
# dd = DrugDog()
# daqiu = Person()
# daqiu.work_with_dog(dd)

class Dog(object):
    __tooth = 10

    @classmethod
    def get_smooth(cls):
        return cls.__tooth




wangcai = Dog()
xiaohei = Dog()
result = wangcai.get_smooth()

print(Dog.get_smooth())
