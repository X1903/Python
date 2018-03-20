# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# 成员运算符 in, not in   返回bool类型
a = 1
a in [1,2,3,4,5]  # True

b = 6
b in [1,2,3,4,5]  # False

b not in [1,2,3,4,5]  # True

b = 'h'
b in 'hello'  # True

# 字典的成员运算符   key值决定
b = 'a'
b in {'c':1}   # False

b = 1
b in {'c':1}   # False

b = 'c'
b in {'c':1}   # True
# key值决定