fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits))
print(sorted(fruits, key=str.lower, reverse=True))
print(fruits)
print(fruits.sort(key=len))  # returns None but saves sort to fruits
print(fruits)
