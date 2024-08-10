class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

p = Programmer("Piyush", 2500000, "ML")
print(p.name, p.company, p.department, p.salary)

         