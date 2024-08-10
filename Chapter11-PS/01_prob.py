class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)  # Pass i and j to the parent class constructor
        self.k = k  # Initialize k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


obj1 = TwoDVector(3, 4)
obj2 = ThreeDVector(1, 2, 5)

obj1.show()  # Output: The vector is 3i + 4j
obj2.show()  # Output: The vector is 1i + 2j + 5k




        
        