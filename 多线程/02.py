import _thread as thread
import time

def loop1():
    print("开始loop1",time.ctime())

    time.sleep(4)

    print("结束loop1",time.ctime())

def loop2():
    print("开始loop2",time.ctime())

    time.sleep(2)

    print("结束loop2",time.ctime())

def main():
    print("主函数开始",time.ctime())



    thread.start_new_thread(loop1,())



    thread.start_new_thread(loop2,())




    print("主函数结束",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)