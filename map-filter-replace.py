# The map, filter, and reduce higher-order functions are still around, but better alternatives are available for most of their use cases, as the next section shows.

from math import factorial

# map
print(list(map(factorial, range(6))))

# can be written as a list comp, much better
print([factorial(n) for n in range(6)])
