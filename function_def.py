#! /usr/bin/env python3
"""
Python3 函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
"""
"""
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
1. 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
2. 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
3. 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
4. 函数内容以冒号 : 起始，并且缩进。
5. return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
"""


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

"""
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如 整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a)）内部修改 a 的值，则是新生成来一个 a。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
"""


def change(immutable_var):
    print(id(immutable_var))  # 指向的是同一个对象
    immutable_var = 10
    print(id(immutable_var))  # 一个新对象


a = 1
print(id(a))
change(a)


# 可写函数说明
def chang_name(mutable_var):
    # 修改传入的列表
    mutable_var.append([1, 2, 3, 4])
    print("函数内取值: ", mutable_var)
    return


# 调用changeme函数
my_list = [10, 20, 30]
chang_name(my_list)
print("函数外取值: ", my_list)

"""
关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
"""


# 可写函数说明
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return


# 调用printme函数
printme(str="菜鸟教程")

"""
默认参数
调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
"""


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")

"""
不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
"""


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)


# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

"""
匿名函数
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

"""
return语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
"""


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

"""
强制位置参数
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
"""


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)

# b 不能使用关键字参数的形式
# f(10, b=20, c=30, d=40, e=50, f=60)
# e 必须使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)
