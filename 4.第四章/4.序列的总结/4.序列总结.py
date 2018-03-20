# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

(1+1)*2
type((1))   # (1)python3当作数学运算

type((1,))  # tuple

type(())    # tuple

type([1])   # list

# int,float,bool,str,list,tuple
# 序列：str,list,tuple

'hello,world'[2]
[1,2,3][2]
# 序列都会被分配到一个序号

# 切片
[1,2,3,4][0:3]
"hello,world"[0:8:2]   # 'hlow'

3 in [1,2,3,4,5,6]     # True
3 not in [1,2,3,4,5,6] # False

len([1,2,3,4,5,6])   # 6
len("hello,world")   # 11

max([1,2,3,4,5,6])   # 6
min([1,2,3,4,5,6])   # 1
max("hello,world")   # w
min("hello,world")   # ,

# 字符编码问题
ord('w')  # 119
ord('d')  # 100
ord(',')  # 44
ord(' ')  # 32