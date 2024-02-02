"""
    协程：
        1. 协程是一个特殊的函数，可以暂停执行，后续可以从暂停的地方继续执行
        2. 协程是单线程的
        3. 协程是用户自己控制的，不是操作系统控制的

        4. 协程的优势：
            1. 协程的执行效率比多线程高
            2. 协程的开销比多线程小
            3. 协程没有锁的概念，不需要考虑锁的问题
            4. 协程的切换是用户自己控制的，不需要操作系统切换
"""
import asyncio  # 异步io模块
async def func():  # 定义一个协程函数
    print("hello")

if __name__ == '__main__': # 判断是否是主模块 RuntimeWarning：从未等待过协程“func” RuntimeWarning: coroutine 'func' was never awaited
    # 协程对象想要执行 需要借助 event_loop
    # coroutine = func()
    # print(coroutine)
    asyncio.run(func())