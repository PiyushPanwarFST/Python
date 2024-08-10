class Employee:
    name = "piyush"

    # def function(self):
    #     print(f"name of the employee is {self.name}") # 
    # result pramod it shows instance attribute

    @classmethod
    def function(cls):
        print(f"name of the employee is {cls.name}") 
        # result piyush it shows class attribute

obj = Employee()
obj.name = "pramod"
obj.function() 
