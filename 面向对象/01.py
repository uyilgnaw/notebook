class PythonStudent():
    # 可以使用None给不确定的值赋值
    name = None
    age = 13
    course = "Python"
    def doHomework(self):
        print("mrking")
        return  None

king = PythonStudent()
print(king.name)
print(king.age)
king.doHomework()