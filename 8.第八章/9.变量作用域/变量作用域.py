# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

c = 50

def add(x,y):
    global b   # 全局作用于,函数外部也可以使用
    c = x + y
    b = x + y

    print(c)

add(1,2)
print(c)
print(b)