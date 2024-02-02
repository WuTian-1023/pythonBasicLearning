from multiprocessing import Process

def f(name):
    for i in range(1000):
        print('hello', name, i)


if __name__ == '__main__':
    # 创建进程
    p = Process(target=f, args=('bob',))
    p1 = Process(target=f, args=('abd',))
    # 启动进程
    p.start()
    p1.start()

# 何时使用多线程，何时使用多线程
# 1.如果任务是IO密集型，任务相对统一，相互特别相似，多线程
# 2.如果任务是计算密集型 多个任务相互独立，很少有交集，多进程