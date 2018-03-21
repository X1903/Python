# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)

squsum(1,2,3,4)

print('\n')

def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
        print(sum)

squsum(1,2,3,4)
print('\n')

squsum(*{1,2,3,4})
print('\n')
# 任意关键字参数
# squsum('36c','42c','31c')   TypeError: can't multiply sequence by non-int of type 'str'
print('\n')

def city_temp(**param):
    for key,value in param.items():
        print(key,':',value)

a = {'bj':'32c','sh':'31c'}
city_temp(bj='32c',xm='23c',sh='31c')
print('\n')

city_temp(**a)
city_temp()
