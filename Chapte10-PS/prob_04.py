class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self,n):
        print(f"the square of {n} is : {self.n * self.n}")

    def cube(self,n):
        print(f"the cube of {n} is : {self.n * self.n * self.n}")

    def squareRoot(self,n):
        print(f"the square root of {n} is: {self.n**1/2}")

    @staticmethod
    def greet(): # no self because no requirement of obj properties 
        print("Hello user")
    
obj = Calculator(4)
obj.greet()
obj.square(4)
obj.cube(4)
obj.squareRoot(4)

        
        