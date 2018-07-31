import multiprocessing

import time

def clock(i):
    while True:
        print("clock运行了" + time.ctime())
        time.sleep(i)


if __name__ == '__main__':
    p=multiprocessing.Process(target=clock,args=(5,))
    p.start()

    while True:
        print("主进程在运行中。。。")
        time.sleep(1)