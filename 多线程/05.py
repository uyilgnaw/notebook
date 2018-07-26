import time

import threading

def fun():
    print("Start fun")

    time.sleep(2)

    print("End fun")

print("主进程开始")

t1=threading.Thread(target=fun)

t1.setDaemon(True)
# 另一种写法：t1.Daemon=True
t1.start()

time.sleep(1)

print("主进程结束")