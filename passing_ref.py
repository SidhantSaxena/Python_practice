class Employee:
    def __init__(self,eno,ename,esal):
        self.ename = ename
        self.eno = eno
        self.esal = esal

    def display(self):
        print(f"Employee name :{self.ename}")
        print(f"Employee no :{self.eno}")
        print(f"Employee salary :{self.esal}")

class Test:
    def __init__(self,emp_ref):
        self.emp_ref = emp_ref

    def Update(self):
        self.emp_ref.esal = self.emp_ref.esal+1000
        self.emp_ref.display()
        print(self.emp_ref.__dict__)  

p1 = Employee(123,"sam",20000)
p1.display()
t = Test(p1)
t.Update()
print(p1.__dict__)



