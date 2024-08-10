class Employee:
    language = "python"
    salary = 120000

    def getInfo(self):
        print(f"the language is {self.language} and the salary ,employee is {self.salary}")

harry = Employee()
harry.getInfo()
# Employee.getInfo(harry)
harry.language = "javascript"
print(harry.language, harry.salary)