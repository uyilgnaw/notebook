import time

import threading

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)


        if m.acquire(1):
            num=num+1
            msg=self.name +'set num to '+ str(num)
            print(msg)

            m.acquire()
            m.release()
            m.release()

num=0
m=threading.RLock()

def TestTh():
    for i in range(5):
        t=MyThread()
        t.start()

if __name__ == '__main__':
    TestTh()
