# _*_ coding:utf-8 _*_
__author__ = 'Xbc'



# 流程控制语句
'''
python靠缩进区分代码段
流程控制语句 
条件控制   循环控制       分支
if else   for  while   switch
选择性问题
'''

a = 1
b = 2

if a > b:
    print('go to left')
else:
    print('go to right')

account = 'qiyue'
password = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if user_account == account:
    if user_password == password:
        print('success')
else:
    print('fail')