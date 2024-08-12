class TwoDVector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("This is a 2D vector")

    def __str__(self):
        return f"{self.a}i + {self.b}j"


class ThreeDVector(TwoDVector):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
        print("This is a 3D vector")

    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"


# Creating a 2D vector
obj1 = TwoDVector(2, 3)
print(obj1)

# Creating a 3D vector
obj2 = ThreeDVector(2, 3, 5)
print(obj2)
