import random
import openpyxl

class A:

    def ran(self):
        e1=openpyxl.load_workbook(filename="C:/Users/meridian/Desktop/随机/42_41.xlsx",read_only=True)
        w1=e1.active
        l1=list(w1.rows)
        l2=list()
        print(len(l1))
        for m in range(200):
            l3 = list()
            r1=random.randint(0,len(l1)-1)
            for i in l1[r1]:

                    l3.append(i.value)


            l2.append(l3)

        #开始写入
        e2=openpyxl.Workbook()
        w2=e2.active

        for i in l2:

            w2.append(i)
            #print(w2['A{0}'.format(i)].value)
        e2.save("C:/Users/meridian/Desktop/随机/已随机42_41.xlsx")

if __name__ == '__main__':
    a=A()
    a.ran()
