# -*- coding:utf-8 -*-
import threading as td
import threadpool as tdp
import multiprocessing as mp
import asyncio
import os

# from multiprocessing import Process
# from multiprocessing import Pipe,Queue
#    Pipe.send
#    Pipe.recv
# from multiprocessing import Lock
#    l=Lock()
#    l.acquire()
#    l.release()

"""
    此模块存放了一些关于多进程\线程的例程
"""

poolsize=16
def exp_of_tdp(func,list_of_args,callback):
    """线程池的使用"""
    pool = tdp.ThreadPool(poolsize)  
    requests=tdp.makeRequests(func,list_of_args,callback)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    


def exp_of_mp(func):
    num_of_process=6
    for j in range(num_of_process):
        p=mp.Process(target=func,args=())
        #进程开始执行
        p.start()
        #进程阻塞，
        p.join()
    
def exp_of_async():
    """
        async 关键字
            对函数进行包装，使其成为协程
            async def func()
        Future
            提供了一个可供操作的载体，可以承载运算结果
            set_result()用于设置结果
            result()用于获得结果
            asyncio.ensure_future(func(Future))
                该函数返回一个task类，
        loop=asyncio.get_event_loop()
            用于捕获包装的函数，同时定义一个可以操作的对象
        await 关键字
            可以使函数暂时挂起直至后续语句执行完毕 
        task=asyncio.wait(funcs)
            用于将异步函数进行打包，task是future的一个子类
            funcs=[]
        loop.run_until_complete(task)
            运行协程
        loop.close()      
    """

    async def  hello_world():
        print("Hello,world!")
        r=await asyncio.sleep(1)
        print("I'm here!")
    async def call():
        print("I'm Bob!")
    
    loop=asyncio.get_event_loop()

    # task=[hello_world(),call()]
    # loop.run_until_complete(asyncio.wait(task))
    # loop.close()
    async def work(future):
        await asyncio.sleep(1)
        future.set_result("future finished!")
    future=asyncio.Future()
    task=asyncio.ensure_future(work(future))
    loop.run_until_complete(task)
    print(future.result())

    loop.close()



def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

def to_know_pid():
    """用于理解多线程中的PID问题"""
    # 
    # if __name__ == '__main__':
    #     info('main line')
    #     for i in range(5):
    #         p = mp.Process(target=f, args=('bob'+str(i),))
    #         p.start()
    #         p.join()
    # 
    pass
if __name__=="__main__":
    #exp_of_async()
    pass
