# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


# 逻辑运算符 and(且) or(或) not(非)
True and True   # True
True and False  # False

True or False   # True
False or False  # False

not False       # True
not True        # False

not not True    # True

1 and 1  # 1
'a' and 'b'  # b
'a' or 'b'  # a
not 'a'  # False
not True # False

# int float 0 被认为是False, 非0 表示True
# 字符串 空字符串 False, True
not ''  # Trur
not '0' #False

# [] 空的列表 False, True
not []   #True
# tuple set dict

not 1
[1] or []
[] or [1]  # 运算的结果到底是True还是False

1 and 0
0 and 1

1 and 2
2 and 1  # 只有第2个值判断结束才能确定

1 or 2
2 or 1
0 or 1
1 or 0  # 能判断结束的时候计算机就会结束判断