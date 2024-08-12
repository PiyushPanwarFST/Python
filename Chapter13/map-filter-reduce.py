# Map Example 
lst = [1,2,3,4,5,6,7,8,9]

square = lambda x: x*x

sqList = map(square, lst)
print(list(sqList))


# Filter Example:
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, lst)
print(list(onlyEven))



# Reduce Example:
from functools import reduce

sum = lambda a,b: a+b
res = reduce(sum, lst)
print(res)


