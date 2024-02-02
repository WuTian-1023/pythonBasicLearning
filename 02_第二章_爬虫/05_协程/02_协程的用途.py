import asyncio
import time


async def func1():
    print("我是func1")
    await asyncio.sleep(1)
    print("func1结束")


async def func2():
    print("我是func2")
    await asyncio.sleep(2)
    print("func2结束")


async def func3():
    print("我是func3")
    await asyncio.sleep(3)
    print("func3结束")


async def main():
    # 创建任务对象
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    task3 = asyncio.create_task(func3())

    # 等待所有任务完成
    await asyncio.wait([task1, task2, task3])


if __name__ == '__main__':
    # 计时
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
