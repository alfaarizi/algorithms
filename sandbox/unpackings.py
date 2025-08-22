# There are two unpacking operators:
# 1. *  : unpacks iterables (lists, tuples, sets, strings, etc)
# 2. ** : unpacks dictionaries (key-value pairs)

# Examples:
# List unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(combined)  # [1, 2, 3, 4, 5, 6]

# Dict unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Function arguments
def add(x, y, z):
   return x + y + z

numbers = [1, 2, 3]
result = add(*numbers)  # Same as add(1, 2, 3)
print(result)  # 6

person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
def greet(name, age, city):
   print(f"Hi {name}, {age} years old, from {city}")

greet(**person)  # Same as greet(name='Alice', age=25, city='NYC')

# *args and **kwargs
def func(*args, **kwargs):
   print("args:", args)      # tuple of positional args
   print("kwargs:", kwargs)  # dict of keyword args

func(1, 2, 3, name="Bob", age=30)
# args: (1, 2, 3)
# kwargs: {'name': 'Bob', 'age': 30}