# 非守护线程
import time
import threading

def fun():
    print("Start fun")

    time.sleep(2)

    print("End fun")

print("主线程")

t1=threading.Thread(target=fun)

t1.start()

time.sleep(1)

print("主线程结束")