class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, num):
        return self.x + num.x

n = Number(1)
m = Number(2)

print(n + m)