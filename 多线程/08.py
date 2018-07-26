import threading
from time import sleep,ctime

loop=[4,2]

class ThreadFunc:
        def __init__(self,name):
            self.name=name

        def loop(self,nloop,nsec):
            print("开始loop",nloop,"at",ctime())
            sleep(nsec)

            print("结束loop",nloop,"at",ctime())

def main():
    print("开始主函数",ctime())
    t=ThreadFunc("loop")
    t1=threading.Thread(target=t.loop,args=("Loop1",4))

    t2=threading.Thread(target=ThreadFunc("loop").loop,args=("loop2",2))

    t1.start()

    t2.start()

    t1.join()
    t2.join()

    print("主函数结束",ctime())

if __name__ == '__main__':
    main()