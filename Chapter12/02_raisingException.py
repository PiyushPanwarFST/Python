a = int(input("enter the 1st number: "))
b = int(input("enter the 2nd number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")