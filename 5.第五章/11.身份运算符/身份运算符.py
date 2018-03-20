# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# 身份运算符 is, is not  返回bool类型
# ==值比较  is内存地址比较
a = 1
b = 2
a is b

a = 1
b = 1
a is b
a == b

a = 1
b = 1.0
a == b  # True
a is b  # False
# == 关系比较是: 值是否相等
# is 不是比较值相等。is 比较的是两个变量的身份是否相等(内存地址)
id(a)
id(b)

a = {1,2,3}
b = {2,1,3}
a == b  # True
a is b  # False

c = (1,2,3)
d = (2,1,3)
c == d  # False
c is d  # False