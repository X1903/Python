# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


a = 1
b = 2
c = 3

a or b ## 1
a and c ## 3
a or b and c ## 1
a or (b and c) ## 1



# 从左向右  左结合


not a or b + 2 == c

(not a) or ((b + 2) == c)

# not > and > or
# 算术运算符 > 比较运算符 > 逻辑运算符
