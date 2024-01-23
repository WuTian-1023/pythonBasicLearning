# aiofiles 是一个异步文件操作库，asyncio 是 Python3.4 之后内置的异步 IO 框架
# aiohttp 是一个异步请求库，asyncio 是 Python3.4 之后内置的异步 IO 框架
# aiohttp 可以与 asyncio 配合使用，实现异步请求
# aiohttp 的使用步骤：
#     1. 创建一个异步请求对象
#     2. 发起请求
#     3. 获取响应数据
#     4. 关闭请求对象
#     5. 关闭事件循环
import aiohttp