import copy


def f(a, b):
    # a = copy.copy(a) copy object to ensure parameter value not changed if mutable
    # b = copy.copy(b)
    print(f'id of a = {id(a)} before assignment')
    a += b
    # a is assigned a new id within f()
    print(f'id of a = {id(a)} after assignment')
    return a


x = 1
y = 2

print(f'id of x = {id(x)}')

print(f(x, y))
print(f'x = {x}')
print(f'y = {y}')

x = [1, 2]
y = [3, 4]
print(f(x, y))
print(f'x = {x}')
print(f'y = {y}')

# When you are coding a function that receives a mutable parameter, you should carefully consider whether the caller expects the argument passed to be changed.
