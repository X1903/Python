# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 类的名字首字母需要大写，不要像变量一样用下划线
# 实例化
# 类最基本的作用：封装
# 类和对象
class Student():


    # '类变量' '实例变量'
    def __init__(self, name, age):  # 实例方法 对象
        # 构造函数
        # 初始化对象的属性
        self.name = name  # 实例变量
        self.age = age
        # print('student')

    # 私有方法  双下划线
    def __marking(self):
        pass

    # 私有方法   外部可以使用
    def __marking__(self):
        pass

    # 公有方法
    def marking(self):
        pass
