import time
import threading

def loop1():
    print("loop1开始",time.ctime())

    time.sleep(4)

    print("loop1结束",time.ctime())

def loop2():
    print("loop2开始",time.ctime())

    time.sleep(2)

    print("loop2结束",time.ctime())

def loop3():
    print("loop3开始",time.ctime())

    time.sleep(5)

    print("loop3结束",time.ctime())

def main():
    print("主程序开始",time.ctime())

    t1=threading.Thread(target=loop1)

    t1.setName("loop1")

    t1.start()

    t2=threading.Thread(target=loop2)
    t2.setName("loop2")
    t2.start()

    t3=threading.Thread(target=loop3)

    t3.setName("loop3")
    t3.start()

    time.sleep(3)

    for i in threading.enumerate():
        print("正在运行的线程名字使{0}".format(i.getName()))
    print("正在运行的线程数量为{0}".format(threading.activeCount()))

    print("主程序结束",time.ctime())

if __name__ == '__main__':
    main()