# Tuples hold records: each item in the tuple holds the data for one field and the position of the item gives its meaning.

# tuple unpacking (iterable unpacking)
lax_coordinates = (33, 12)
latitude, longitude = lax_coordinates

print(f'{latitude}, {longitude}')


# unpacking with *argument
def printCoordinates(a, b):
    return a, b


# return multiple values that can be unpacked by caller
a, b = printCoordinates(*lax_coordinates)
print(f'{a}, {b}')

# * to grab excess items
a, b, *rest = range(5)

print(f'{a}, {b}, {rest}')

# tuples are immutable the exception is if they contain mutable objects
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(id(a))
print(id(b))
print(a is b)
print(a == b)

# update list inside tuple
b[-1].append(99)
print(id(b))
print(a == b)
print(b)

# check if tuple contains mutable objects with hash, mutable object will throw TypeError: unhashable type
# print(hash(a))
