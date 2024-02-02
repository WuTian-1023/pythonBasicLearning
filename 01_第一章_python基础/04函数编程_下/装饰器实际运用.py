login_status = False # 登录状态


def login_verify(func):
    def inner(*args, **kwargs):
        global login_status  # 引入全局变量
        if not login_status:  # 如果没有登录
            while 1:  # 死循环
                print('登录验证')
                loginName = input('请输入用户名：')
                password = input('请输入密码：')
                if loginName == 'admin' and password == '123456':
                    print('登录成功')
                    login_status = True
                    break
                else:
                    print('登录失败')
        ret = func(*args, **kwargs)  # 执行被装饰的函数
        return ret

    return inner


@login_verify
def add():
    print('add函数')


@login_verify
def delete():
    print('delete函数')


@login_verify
def update():
    print('update函数')


@login_verify
def select():
    print('select函数')


add()
delete()
