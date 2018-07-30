import threading

import time

lock_1=threading.Lock()

lock_2=threading.Lock()

def func_1():
    print("func_1 starting.....")
    lock_1.acquire()
    print("func_1 申请了lock_1")
    time.sleep(2)
    print("fun_1将要申请lock_2")
    lock_2.acquire()
    print("func_1申请了lock2")
    lock_2.release()
    print("lock_2释放了")
    lock_1.release()
    print("lock_1释放了")
    print("func_1 做完了")

def func_2():
    print("func_2开始了")
    lock_2.acquire()
    print('lock_2申请成功')
    time.sleep(4)
    print("func_2将要申请lock_1")
    lock_1.acquire()
    print("func_2申请了lock_1")
    lock_1.release()
    print("lock_1释放了")

    lock_2.release()
    print("lock_2释放了")

    print("func_2结束了")

if __name__ == '__main__':
    print("住程序开始了")
    t1=threading.Thread(target=func_1,args=()) # 此参数有个问题，不能带括号。

    t2=threading.Thread(target=func_2,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("住程序结束了")
