class Employee():
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

obj1 = Employee()
print(obj1.a)

obj2 = Programmer()
print(obj2.a, obj2.b)

obj3 = Manager()
print(obj3.a, obj3.b, obj3.c)




