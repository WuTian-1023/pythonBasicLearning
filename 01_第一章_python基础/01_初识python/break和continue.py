# 停止当前循环  break
while True:
    content = input("请输入你要输入的内容:")
    print("发送给对抗路:",content);
    if content != "":
        break
print("GG,游戏结束!")

# 停止本次循环,进入下次循环
i = 1
while i <= 10:
    if i == 7:
        i += 1
        continue
    print(i)
    i +=1