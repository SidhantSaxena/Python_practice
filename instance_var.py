class Test:
    a = 123
    def __init__(self):
        self.a = 12
        self.b = 14
    def display(self):
        print(" ",self.a)
        print(self.b)
        print(Test.a)


t1 = Test()
print(t1.a)
t1.display()
