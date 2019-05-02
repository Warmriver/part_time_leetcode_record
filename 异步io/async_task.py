import time
import asyncio
from urllib.request import urlopen

async def foo():
    print("hello")

def go():
    print("begin")
    loop = asyncio.get_event_loop()
    task = loop.create_task(foo())
    loop.run_until_complete(task)
    elap_time(3)
    print("done")

def elap_time(n):
    start = time.time()
    now = start
    while now < start + n:
        now = time.time()

async def async_elapse_time(n):
    # time.sleep(2)
    await asyncio.sleep(2)
    print("counting ", n, " complete")



async def main():
    print("begin")
    task1 = asyncio.create_task(async_elapse_time(3))
    task2 = asyncio.create_task(async_elapse_time(3))
    await task1
    await task2
    
    print("done")


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

# 协程（xc）允许程序员在代码层面充分控制xc的行为，选择何时挂起。xc可以挂起自己，一般是在耗时操作上，挂起后cpu时间片可以分给其他xc。 这里的耗时操作需要是异步的，如果是同步的，那么整个方法仍然是同步的
def test_web():
    loop = asyncio.get_event_loop()
    # t1 = f("https://www.zhihu.com")
    # t2 = f("https://www.python.org/")
    # t3 = f("https://www.baidu.com/")
    f1 = loop.run_in_executor(None, f, "https://www.zhihu.com")
    f2 = loop.run_in_executor(None, f, "https://www.python.org/")
    f3 = loop.run_in_executor(None, f, "https://www.baidu.com/")
    loop.run_until_complete(asyncio.wait([f1, f2, f3]))
    print("done")
    f1 = loop.run_in_executor(None, f, "https://www.github.com")



    # tasks = [t1,t2,t3]
    # loop.run_until_complete(asyncio.wait(tasks))



if __name__ == '__main__':
    test_web()
