import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return what


async def main():
    f1 = say_after(3, 'hello')
    f2 = say_after(2, 'world')
    f3 = say_after(1, 'python')
    tasks = [asyncio.create_task(f1), asyncio.create_task(f2), asyncio.create_task(f3)]

    # done, pending = await asyncio.wait(tasks) # 等待所有任务完成 done是已完成的任务 pending是未完成的任务
    # # print(done)
    # for t in done:
    #     print(t.result()) # 获取任务的返回值 顺序乱了

    # gather和wait的区别 gather更加高级 一般用gather 返回值按照 任务传入的顺序
    # 等待所有任务完成 并获取返回值
    # return_exceptions=False 如果某个任务出错了 所有任务停止 并抛出异常
    # return_exceptions=True 如果某个任务出错了 不影响其他任务的执行 并抛出异常
    result = await asyncio.gather(*tasks, return_exceptions=False)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())