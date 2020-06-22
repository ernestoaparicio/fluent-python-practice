import collections
from collections import abc

my_dict = {}

print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))

# dict comprehensions
dial_codes = [(880, 'Bangladesh'), (55, 'Brazil')]

# dict comprehension by looping and tuple unpacking
country_dial = {country: code for code, country in dial_codes}

# get values, set default if key missing
print(country_dial.get(3, {'country': 'USA'}))

# setDefault example
index = {}

for x in range(10):
    index.setdefault(x, []).append(f'{x} index')

print(index)

# alternative to setDefault
key = 0
if key not in index:
    index[key] = []
    index[key].append(f'{x} index')

print(index)

# using defaultdict to set default empty list and avoid KeyError

index = collections.defaultdict(list)
for x in range(10):
    index[x].append(f'{x} index')

print(index)

# using defaultdict to set default empty tuple and avoid KeyError

index = collections.defaultdict(tuple)
for x in range(10):
    index[x] = (f'{x} index')

print(len(index))
