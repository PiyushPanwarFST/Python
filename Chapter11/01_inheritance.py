class Employee:
    name = "Piyush"
    def sample(self):
        print(f"the name of emplyee is {self.name}")


class Programmer(Employee):
    language = "python"
    def sample(self):
        print(f"{self.name} is working on {self.language} project")

obj1 = Programmer()
obj1.sample()

obj2 = Employee()
obj2.sample()
 
