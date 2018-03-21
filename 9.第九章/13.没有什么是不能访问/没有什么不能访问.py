
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