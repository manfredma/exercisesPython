import keyword

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

print(keyword.kwlist)

if True:
    print("True")
else:
    print("False")

item_one = "3"
item_two = "3"
item_three = "3"
total = item_one + \
        item_two + \
        item_three
print(total)

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

strE = 'Runoob'

print(strE)  # 输出字符串
print(strE[0:-1])  # 输出第一个到倒数第二个的所有字符
print(strE[0])  # 输出字符串第一个字符
print(strE[2:5])  # 输出从第三个开始到第五个的字符
print(strE[2:])  # 输出从第三个开始后的所有字符
print(strE[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
print(strE * 2)  # 输出字符串两次
print(strE + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

'''
空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。
但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
'''

# 等待用户输入
'''
input("\n\n按下 enter 键后退出。")
'''
# 同一行显示多条语句
import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

# 多个语句构成代码组
'''
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
'''

# print
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

