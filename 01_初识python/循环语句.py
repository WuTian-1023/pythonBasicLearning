# while True 死循环
# 用程序去数1-100
# i = 1;
# while i < 101:
#     print(i)
#     i+=1

# 1+2+3 .....
i = 1
s = 0
while i <= 100:
    s = s + i
    i = i + 1
print(s)

# for循环
str = "我是超人强,越超人越强"
for c in str:
    print(c)
# 从1到100 一次进1  从m->n 不包含n
for i in range(1, 101, 1):
    print(i)
