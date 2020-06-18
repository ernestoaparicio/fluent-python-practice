from collections import abc

my_dict = {}

print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))

# dict comprehensions
dial_codes = [(880, 'Bangladesh'), (55, 'Brazil')]

# dict comprehension by looping and tuple unpacking
country_dial = {country: code for code, country in dial_codes}
