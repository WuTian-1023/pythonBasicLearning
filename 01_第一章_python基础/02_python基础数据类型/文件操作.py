import os
import time
"""
 1.找到文件
"""
# f = open("国产自拍.txt", "r", encoding="utf-8")
# print(f.read())
# f.close()
"""
2.读取文件
    read() 读取所有内容
    readline() 读取一行 一次一行 
    readlines() 读取所有行
"""
# f = open("国产自拍.txt", "r", encoding="utf-8")
# print(f.read(2))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()
"""
3.写入文件
    write()
    writelines()
"""
f = open("国产自拍.txt", "w", encoding="utf-8")
f.write("你好啊\n")
f.writelines(["你好啊\n", "你好啊\n", "你好啊\n"])
f.close()
"""
4.文件的其他操作
    seek() 移动光标
    tell() 获取光标的位置
"""
# f = open("test.txt", "r", encoding="utf-8")
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# f.seek(0)
# print(f.tell())
# f.close()
"""
5.文件的上下文管理器
"""
# with open("test.txt", "r", encoding="utf-8") as f:
#     print(f.read())
"""
6.文件的模式
    r 只读
    w 只写
    a 追加
    r+ 读写
    w+ 读写
    a+ 读写
"""
# with open("test.txt", "a+", encoding="utf-8") as f:
#     f.write("你好啊\n")
#     f.seek(0)
#     print(f.read())
"""
7.文件的其他参数
    encoding 编码
    newline 换行
"""
# with open("test.txt", "a+", encoding="utf-8", newline="\n") as f:
#     f.write("你好啊\n")
#     f.seek(0)
#     print(f.read())
"""
8.文件的读取方式
    t 文本方式
    b 二进制方式
"""
with open("1.jpg", "rb") as f:
    print(f.read())
"""
9.文件的读取位置 
"""
# 文件的复制
with open("1.jpg", "rb") as f:
    with open("2.jpg", "wb") as f1:
        f1.write(f.read())

# 文件的修改
# 在源文件中把文件中的所有周换成田
with open("人名.txt", "r", encoding="utf-8") as f:
    with open("人名1.txt", "w", encoding="utf-8") as f1:
        for line in f:
            f1.write(line.replace("周", "田"))
time.sleep(2)
os.remove("人名.txt")
time.sleep(2)
os.rename("人名1.txt", "人名.txt")


