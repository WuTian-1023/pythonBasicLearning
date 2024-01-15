"""
内容回顾：
    1.函数可以作为参数传递
    2.函数可以作为返回值返回
    3.函数名称可以作为变量使用

装饰器：
        本质上就是一个闭包函数
        作用：在不修改原函数的代码以及调用方式的前提下为原函数增加新的功能

        用户登录的验证，日志记录，性能测试，事务处理，权限校验等场景
        雏形：
            def wrapper(fn):
                def inner(*args, **kwargs):
                    ret = fn(*args, **kwargs)
                    return ret
                return inner

        语法糖：@ + 函数名 就是装饰器

"""


def func():
    print("我是func函数")


def func2(a):
    a()


func2(func)


def func3():
    def inner():
        print("我是inner函数")

    return inner


ret = func3()
ret()  # 调用inner函数


def play_game2(a):
    def inner():
        print("开始玩游戏")
        a()
        print("结束玩游戏")

    return inner


def func4():
    print("我是func4函数")


def func5():
    print("我是func5函数")


func4 = func5  # 将func5函数赋值给func4
func4()  # 调用func5函数


def play_dnf():
    print("玩dnf")


def play_wzry():
    print("玩王者荣耀")


@play_game2  # @ + 函数名 就是装饰器
def play_jdqs():
    print("玩绝地求生")


def play_lol():
    print("玩英雄联盟")


def play_game(a):
    print("开始玩游戏")
    a()  # 调用传递的函数
    print("结束玩游戏")


play_game(play_dnf)

play_wzry = play_game2(play_wzry)  # 让play_wzry变量指向inner函数
game_lol = play_game2(play_lol)
play_wzry()  # 调用inner函数
game_lol()

play_jdqs()


#######################参数

def play_game3(a):
    def inner(username, password):
        print("开始玩游戏")
        a(username, password)
        print("结束玩游戏")

    return inner


def play_game4(a):
    def inner(*args, **kwargs):  # *args, **kwargs 代表接收任意参数 *， ** 打包成元组和字典
        print("开始玩游戏")
        a(*args, **kwargs)  # * + 变量名 代表拆包
        print("结束玩游戏")

    return inner


@play_game3
def play_wzry(username, password):
    print("玩王者荣耀", username, password)


play_wzry("alex", "123456")


@play_game4
def play_lol(username, password, hero):
    print("玩英雄联盟", username, password, hero)


play_lol("alex", "123456", "盖伦")


###########返回值
def play_game5(a):
    def inner(*args, **kwargs):  # *args, **kwargs 代表接收任意参数 *， ** 打包成元组和字典
        print("开始玩游戏")
        ret = a(*args, **kwargs)
        print("结束玩游戏")
        return ret
    return inner
@play_game5
def play_lol():
    print("玩英雄联盟")
    return "人在塔在"


lol  = play_lol()
print(lol)

##########一个函数被多个装饰器装饰
print("一个函数被多个装饰器装饰###########################")
def wrapper1(fn):
    def inner(*args, **kwargs):
        print("正在验证权限")
        ret = fn(*args, **kwargs)
        print("权限验证完毕")
        return ret
    return inner
def wrapper2(fn):
    def inner(*args, **kwargs):
        print("正在验证日志")
        ret = fn(*args, **kwargs)
        print("日志记录完毕")
        return ret
    return inner

@wrapper1 # play_lol = wrapper1(play_lol)
@wrapper2 # play_lol = wrapper2(play_lol) play_lol = wrapper1(wrapper2(play_lol))
def play_lol():
    print("玩英雄联盟")
    return "人在塔在"


play_lol1 = play_lol()
print(play_lol1)
"""
结果：   1.正在验证权限
        2.正在验证日志
        3.玩英雄联盟
        4.日志记录完毕
        5.权限验证完毕
        6.人在塔在
规则： wrapper1进去 wrapper2进去 play_lol进去 play_lol出来 wrapper2出来 wrapper1出来 
"""