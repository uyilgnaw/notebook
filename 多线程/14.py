import threading
import time

def func():
    print("func开始了")
    time.sleep(4)
    print("func结束了")

if __name__ == '__main__':
    t=threading.Timer(6,func)
    t.start()
    i=0
    while True:
        print("主线程{0}".format(i))
        time.sleep(3)
        i +=1