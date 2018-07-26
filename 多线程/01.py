import time

def loop1():
    print("开始Loop1",time.ctime())

    time.sleep(4)

    print("结束Loop1",time.ctime())


def loop2():
    print("开始loop2",time.ctime())

    time.sleep(2)

    print("结束loop2",time.ctime())

def main():
    print("主程序开始",time.ctime())

    loop1()

    loop2()

    print("主程序结束",time.ctime())


if __name__ == '__main__':
    main()