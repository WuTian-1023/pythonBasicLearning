from threading import Thread


def func(name):
    for i in range(10):
        print(name, i)

# 单线程效果
if __name__ == '__main__':
    # 创建线程
    t1 = Thread(target=func, args=("刘德华",))
    t2 = Thread(target=func, args=("王力宏",))
    t3 = Thread(target=func, args=("周润发",))

    # 启动线程
    t1.start()
    t2.start()
    t3.start() # 三个线程同时执行