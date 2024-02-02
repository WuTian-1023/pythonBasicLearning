
def func(name):
    for i in range(10):
        print(name, i)

# 单线程效果
if __name__ == '__main__':
    func("刘德华")
    func("张学友")
    func("周星驰")