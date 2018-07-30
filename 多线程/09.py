import threading

sum=0
loopSum=100000

def myAdd():
    global  sum,loopSum
    for i in range(1, loopSum):
        sum += 1
        print(sum)

def myMinu():
    global sum,loopSum
    for i in range(1, loopSum):
        sum -= 1
        print(sum)

#if __name__ == '__main__':
#    myAdd()
 #   print(sum)
  #  myMinu()
   # print(sum)

if __name__ == '__main__':
    print("现在的sum是{0}".format(sum))

    t1=threading.Thread(target=myAdd,args=())
    t2=threading.Thread(target=myMinu,args=())

    t1.start()

    t2.start()

    t1.join()
    t2.join()
    print("现在的sum是{0}".format(sum))

