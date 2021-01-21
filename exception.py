#! /usr/bin/env python3
"""
异常
即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:
"""
# x = 10 * (1/0)

while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

import sys

try:
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
except:
    pass

"""
try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。
"""
try:
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()
except IOError:
    pass

"""
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。
"""
try:
    runoob()
except NameError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

"""
抛出异常
Python 使用 raise 语句抛出一个指定的异常。
raise语法格式如下：
raise [Exception [, args [, traceback]]]
"""
try:
    x = 10
    if x > 5:
        raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
except:
    print("Unexpected error:", sys.exc_info()[0])
    pass;

"""
预定义的清理行为
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:
for line in open("myfile.txt"):
    print(line, end="")
以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。
"""
for line in open("exception.py"):
    print(line, end="")

with open("exception.py") as f:
    for line in f:
        print(line, end="")
