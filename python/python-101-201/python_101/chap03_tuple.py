# TUPLE (Immutable Sequence)

# Empty tuples (not recommended)
empty_tuple_par = ()
empty_tuple_obj = tuple()

# Initialization of tuples
numtup = (1, 2, 3)
print(numtup)
strtup = ('a', 'b', 'c')
print(strtup)
miscup = ('1', 'a', 1)
print(miscup)

# Convert a list to tuple
nums = [1, 2]
pair = tuple(nums)
print(pair)

# Convert a tuple to list
triple = (4, 5, 6)
numlist = list(triple)
print(numlist)

# Length of a tuple
print(len((1, 2, 3, 4, 5, 6, 7)))  # 7

# Test if an element is inside tuple
print(5 in triple)  # True
print(1 in triple)  # False
print(5 not in triple)  # True
print(1 not in triple)  # False

# Access elements (0-based index)
print(triple[1])

# Tuple Slices
tupsev = (1, 2, 3, 4, 5, 6, 7)
print(tupsev[:])
print(tupsev[2:5])
print(tupsev[:5])
print(tupsev[2:])
print(tupsev[:-2])

# Repeat tuples
nine = 3 * triple
print(nine)

# Find an element in tuple
print(tupsev.index(3))
# print(tupsev.index(1000)) => Exception: not in tuple
