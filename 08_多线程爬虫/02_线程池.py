import time
from concurrent.futures import ThreadPoolExecutor

def func(name):
    for i in range(10):
        print(name, i)

def func2(name, t):
    time.sleep(t)
    print(f"我是{name}")
    return name

def fn (ret):
    print(ret.result())


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t: # 创建一个线程池 ThreadPoolExecutor(10) 10个线程
        for i in range(100):
            # t.submit(func, f"刘德华{i}")
            # t.submit(func2, f"刘德华{i}", 2).add_done_callback(fn) # 回调函数
            # t.submit().add_done_callback 返回即执行 callback函数
            t_map = t.map(func2, ["刘德华", "张学友", "周星驰"], [3, 1, 2])
            for r in t_map:
                print(r)