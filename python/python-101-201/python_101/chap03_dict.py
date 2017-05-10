# DICTIONARY (Hash Table - Immutable key, Mutable value)
# Keys must be hashable (and immutable). List, dictionaries, or mutable objects are not for keys.

# Empty dict
x = {}
print(type(x))
x = dict()
print(type(x))

# Initialize dict
x = {15: 16, 17: 18}  # key = num, val = num
print(x)
x = {'fifteen': 16, 'seven': 18}  # key = str, val = num
print(x)
x = dict(zip(['one', 'two', 'three'], ['four', 'five', 'six']))  # 1 list of keys and 1 list of values
print(x)
x = dict([(15, 16), (17, 18)])  # list of pairs (MUST be tuple-2)
print(x)
x = dict(one='yolo', two=1, three=(1, 2, 3), four=[5, 6, 7])  # applied when keys are strings only
print(x)
x = {(1, 2): [3, 4, 5], (3, 4): [6, 7, 8]}  # key = tuple, val = list
print(x)
x = {15: 'fifteen', '16': 16, (1, 7): [1, 7]}  # misc keys and values
print(x)

# Number of elements inside dict
print(len(x))

# Access value via key (exception if no key present)
print(x[15])
print(x['16'])
print(x[(1, 7)])

# Access value via key (return None or default value)
print(x.get(15))
print(x.get(99))

# Set new values to given key (create new pair if key is not present)
x[15] = ('yolo', 'lolo')
x[19] = 1
print(x)

# Update dictionary
x.update({15: 19, 19: 100, 'hello': 'world'})
print(x)
x.update(hello='doom')  #  applied to keys as strings only
print(x)

# Remove a pair of key-value in dict
del x[19]
print(x)

# Remove a pair of key-value in dict and return that one (exception if key is not present)
print(x.pop('16'))

# Remove an arbitrary pair of key-value and return that one (exception if dict is empty)
print(x.popitem())

# Test if a key is in the dict
print(15 in x)
print(15 not in x)

# Create an iterable collection of keys from dictionary
for key in iter(x):
    print(f"{key} - {x[key]}")

# DICTIONARY VIEW

# A view of dict objects in terms of tuple (key, value) (also changes when elements change)
for element in x.items():
    print(element)

# A view of dict keys (also changes when elements change)
for element in x.keys():
    print(element)

# A view of dict values (also changes when elements change)
for element in x.values():
    print(element)

# Length of a view
x = x.values()
print(len(x))

# Test if an element in dict
print(15 in x)
