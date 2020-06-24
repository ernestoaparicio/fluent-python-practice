from collections import namedtuple
import typing

# Here is a Coordinate class built with namedtuple—a factory function that builds a subclass of tuple with the name and fields you specify:
Coordinate = namedtuple('Coordinate', 'lat long')

moscow = Coordinate(55.756, 37.617)
print(moscow)

Person = namedtuple('Person', 'fname lname age')

ea = Person("Ernie", "Aparicio", "43")
ea2 = Person("Ernie", "Aparicio", "43")
ma = Person("Matt", "Aparicio", "5")

print(ea)
print(ea.age)
print(ea == ea2)
print(ma)

# The newer typing.NamedTuple provides the same funcionality, adding a type annotation to each field:
Person_Typed = typing.NamedTuple('Person_Typed', fname=str, lname=str, age=int)

ea_typed = Person_Typed("Ernie", "Aparicio", 43)
print(ea_typed)
print(ea == ea_typed)