class Employee:
    name = "Piyush"
    def sample(self):
        print(f"the name of emplyee is {self.name}")


class Programmer():
    language = "python"
    def sample(self):
        print(f"he is working on {self.language} project")


class Coder(Employee, Programmer):
    company = "InViedo"
    def sample(self):
        print(f"{self.name} has recently join the {self.company} and woking on {self.language} project")


obj1 = Programmer()
obj1.sample()

obj2 = Employee()
obj2.sample()

obj3 = Coder()
obj3.sample()
 
