class  Student():
    def __init__(self,name="mrking",age=16):
        self.name=name
        self.age=age
    def say(self):
        print("泥嚎，{0}".format(self.name))
def Work():
    print("我是跟Student类平级的函数")
print("我是跟上面两个货平级的输出")


stu=Student()
stu.say()