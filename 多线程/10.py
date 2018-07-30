import threading

sum=0

loopSum=100000

lock=threading.Lock()

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        lock.acquire()
        sum +=1
        #print(sum)
        lock.release()

def myMinu():
    global sum,loopSum
    for i in range(1,loopSum):
        lock.acquire()
        sum -=1
        #print(sum)
        lock.release()


if __name__ == '__main__':
    print("此时的sum{0}".format(sum))
    t1=threading.Thread(target=myAdd,args=())
    t2=threading.Thread(target=myMinu,args=())

    t1.start()

    t2.start()

    t1.join()
    t2.join()


    print("此时的sum是{0}".format(sum))