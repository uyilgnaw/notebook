from multiprocessing import Process

import os

def info(t):
    print(t)
    print('module name',__name__)
    print('父进程位',os.getppid())

    print('进程id位',os.getpid())

def g(n):
    info('我是函数g的info')
    print('你好',n)

if __name__ == '__main__':
    info('我是主进程的info')

    p=Process(target=g,args=('我是紫禁城',))
    p.start()
    p.join()