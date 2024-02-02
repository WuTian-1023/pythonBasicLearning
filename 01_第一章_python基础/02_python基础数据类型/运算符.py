"""
1.算出运算
     + - * / %
2.比较运算
3.赋值运算
4.逻辑运算
5.成员运算
"""
# 1.算出运算
a = 1
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# 互换
# 方法一：使用临时变量
a = 1
b = 2
print(f"原始值：a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"互换后的值：a = {a}, b = {b}")

# 方法二：使用Python的多重赋值
a = 1
b = 2
print(f"原始值：a = {a}, b = {b}")

a, b = b, a
print(f"互换后的值：a = {a}, b = {b}")

# 2.比较运算
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
# 3.赋值运算
a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)
# 4.逻辑运算
a = 1
b = 2
print(a > b > a)
print(a > b or b > a)
print(not a > b)
# 5.成员运算
lst = ["赵本山", "王大拿", "大张伟", "马大哈"]
print("赵本山" in lst)
print("赵本山" not in lst)
# 6.身份运算
a = 1
b = 1
print(a is b)
print(a is not b)
# 7.位运算
# 8.运算符的优先级
print(2 + 3 * 4)
print((2 + 3) * 4)
# 9.运算符的结合性
# 运算符的结合性：当在一个表达式中有多个相同优先级的运算符时，结合性决定了运算符的执行顺序。
# 大多数运算符都是从左到右结合的，也就是说，它们会先处理左边的操作数。例如，100 / 10 / 5 的结果是2，而不是50。
# 10.运算符的短路逻辑
a = 1
b = 2
print(a > b > a)  # 逻辑运算符短路逻辑
print(a < b or b > a)
print(not a > b)
# 运算符的优先级
print(2 + 3 * 4)  # 输出14，因为乘法的优先级高于加法

# 运算符的结合性
print(100 / 10 / 5)  # 输出2，因为除法是从左到右结合的

# 运算符的短路逻辑
a = False
b = True
print(a and b)  # 输出False，因为and的左边的表达式为False，所以整个表达式就为False，右边的表达式不会被执行
print(a or b)  # 输出True，因为or的左边的表达式为False，但是or的右边的表达式为True，所以整个表达式为True
