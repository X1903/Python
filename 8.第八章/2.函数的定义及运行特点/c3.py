# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# R Skill1 Skill2

def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1,damage2

damages = damage(3,6)

skill1_damage,skill2_damage = damage(3,6)
# 序列解包

print(damages[0],damages[1])        # 9 22
print(type(damages))                # <class 'tuple'>

print(skill1_damage,skill2_damage)  # 9 22
