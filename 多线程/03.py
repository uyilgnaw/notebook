import time
import threading

def loop1():
    print("开始loop1",time.ctime())

    time.sleep(4)

    print("结束loop1",time.ctime())

def loop2():
    print("开始loop2",time.ctime())

    time.sleep(2)

    print("结束loop2",time.ctime())

def main():
    print("主程序开始",time.ctime())

    t1=threading.Thread(target=loop1)

    t1.start()

    t2=threading.Thread(target=loop2)

    t2.start()
    # 加入join使主函数等待，当对应的分支线程运行结束后才向下继续执行
    t1.join()

    t2.join()
    print("主程序结束",time.ctime())

if __name__ == '__main__':
    main()


