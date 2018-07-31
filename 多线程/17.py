import multiprocessing

from time import sleep,ctime

class ClockProcess(multiprocessing.Process):
    '''
    其中的两个函数比较重要
    1.构造函数__init__
    2.执行函数run

    '''
    def __init__(self,i):
        super().__init__()
        self.i=i

    def run(self):
        while True:
            print("紫禁城开始了》》》》》")
            sleep(self.i)

if __name__ == '__main__':
    p=ClockProcess(3)
    p.start()
    while True:
        print("主进程开始了？？？？？")
        sleep(1)