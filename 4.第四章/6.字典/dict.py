

## 字典  Ket  Value

type({1:1,2:2,3:3}) ## class 'dict'

{'Q':'新月打击','W':'苍白之瀑','E':'月之降临','R':'月神冲刺'}['Q']  ## '新月打击'

# 不能有重复的键
{'Q':'新月打击','Q':'苍白之瀑','E':'月之降临','R':'月神冲刺'}['Q']  ## '苍白之瀑'

## 字典中不能出现相同的key
{'Q':'新月打击','W':'苍白之瀑','E':'月之降临','R':'月神冲刺'}  ## {'Q':'苍白之瀑','E':'月之降临','R':'月神冲刺'}

## 字典的key必须是不可变的类型  int str
d1 = {1:'新月打击', '1':'苍白之瀑','E':'月之降临','R':'月神冲刺'} ## {1:'新月打击','1:'苍白之瀑','E':'月之降临','R':'月神冲刺'}

d2 = {[1,2]:'新月打击', 1:'苍白之瀑','E':'月之降临','R':'月神冲刺'} ## {1:'新月打击','1:'苍白之瀑','E':'月之降临','R':'月神冲刺'} ## traceback

## 空的字典
type({}) ## class 'dict'


