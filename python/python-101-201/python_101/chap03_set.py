# SET and FROZENSET (Mutable unordered collection of distinct objects)

# Empty Set
empty_set_obj = set()

# Initialization of Set
numset = {1, 2, 3}
print(numset)
strset = {'a', "b", '''c'''}
print(strset)
miscset = {1, 'a', '3'}
print(miscset)
dupset = {1, 2, 3, 3, 3}
print(dupset)

# Number of elements in set
print(len(numset))  # 3

# Test if an element is inside a set
print(1 in numset)  # True
print(0 in numset)  # False
print(1 not in numset)  # False
print(0 not in numset)  # True

# Test if a set is a subset of another one (also applied to list, tuple, frozenset)
print(numset.issubset({1, 3, 2, 5, 4, 6}))  # True
print(numset.issubset({1, 2, 4}))  # False
print(numset.issubset({9, 10, 11, 12}))  # False
print(numset.issubset([1, 3, 2, 5, 4, 6]))  # True
print(numset.issubset((1, 2, 4)))  # False
print(numset.issubset(frozenset([9, 10, 11, 12])))  # False
# Operator "<=" can also be used instead of issuperset
print(numset <= {1, 3, 2, 5, 4, 6})  # True
print(numset <= {1, 2, 3})  # True

# Test if a set is a PROPER subset of another (== must NOT happen)
print(numset < {1, 2, 3, 4})  # True
print(numset < {1, 2, 3})  # False

# Test if a set is a superset of another one (also applied to list, tuple, frozenset)
superset = {1, 3, 2, 5, 4, 6}
print(superset.issuperset(numset))  # True
print(superset.issuperset((1, 2, 3)))  # True
superset = {1, 2, 4}
print(superset.issuperset(numset))  # False
print(superset.issuperset([1, 2, 3]))  # False
superset = {9, 10, 11, 12}
print(superset.issuperset(numset))  # False
print(superset.issuperset(frozenset([1, 2, 3])))  # False
# Operator ">=" can also be used instead of issuperset
print({1, 2, 3} >= {1, 2, 3})  # True
print({1, 2, 3, 4} >= {1, 2, 3})  # True

# Test if a set is a PROPER superset of another (== must NOT happen)
print({1, 2, 3} > numset)  # False
print({1, 2, 3, 4} > numset)  # True

# Test if a set is disjoint with another one (disjoint = no common elements)
print(numset.isdisjoint({1, 4, 5}))  # False
print(numset.isdisjoint({9, 10 , 11}))  # True

# Union of multiple sets
print({1, 2, 3}.union({4, 5, 6}, {5, 6, 7}))
print({1, 2, 3} | {4, 5, 6} | {5, 6, 7})
# Method "union" can also be applied to list, tuple, frozenset
print({1, 2, 3}.union([4, 7, 8], (4, 5, 6), frozenset([10, 11, 12])))

# Intersection of multiple sets
print({1, 2, 3, 4, 5}.intersection({1, 3, 9, 10}, {3, 5, 7}))
print({1, 2, 3, 4, 5} & {1, 3, 9, 10} & {3, 5, 7})
# Method "intersection" can also be applied to list, tuple, frozenset
print({1, 2, 3, 4, 5}.intersection([1, 2, 3], (2, 3, 4), frozenset([1, 3, 5])))

# Difference of multiple sets
print({1, 2, 3, 4, 5}.difference({1, 2, 9, 10}, {3, 4, 10, 12}))
print({1, 2, 3, 4, 5} - {1, 2, 9, 10} - {3, 4, 10, 12})
# Method "difference" can also be applied to list, tuple, frozenset
print({1, 2, 3, 4, 5}.difference([1, 9], (2, 6), frozenset([3, 5, 7])))

# Symmetric Difference of multiple sets (Exclusive Or)
print({1, 2, 3, 4, 5}.symmetric_difference({1, 2, 9}))
print({1, 2, 3, 4, 5} ^ {1, 2, 9})
# Method "symmetric_difference" can also be applied to list, tuple, frozenset
print({1, 2, 3, 4, 5}.symmetric_difference([1, 2, 9]))
print({1, 2, 3, 4, 5}.symmetric_difference((1, 2, 9)))
print({1, 2, 3, 4, 5}.symmetric_difference(frozenset([1, 2, 9])))

# Copy the whole set
cpy = numset.copy()
print(cpy)

# SET ONLY

# In-place Union
uset = {1, 2, 3}
uset.update({2, 3, 4}, {5, 6, 7})
print(uset)
uset |= {0, 9, 8}
print(uset)
# Method "union" can also be applied to list, tuple, frozenset
uset.update([11], (12, 14), frozenset([13]))
print(uset)

# In-place Intersection
uset = {1, 2, 3}
uset.intersection_update({2, 3, 4}, {3, 4, 5})
print(uset)
uset = {1, 2, 3}
uset &= {2, 3, 4} & {3, 4, 5}
print(uset)
# Method "intersection_update" can also be applied to list, tuple, frozenset
uset = {1, 2, 3, 4, 5}
uset.intersection_update([1, 2, 3], (2, 3, 4), frozenset([2, 3, 6]))
print(uset)

# In-place Difference
uset = {1, 2, 3, 4, 5}
uset.difference_update({2, 3, 9}, {1, 4, 10})
print(uset)
uset = {1, 2, 3, 4, 5}
uset -= {2, 3, 9} | {1, 4, 10}
print(uset)
# Method "difference_update" can also be applied to list, tuple, frozenset
uset = {1, 2, 3, 4, 5}
uset.difference_update([2], (3, 4), frozenset([5]))
print(uset)

# In-place Difference Symmetric (Exclusive Or)
uset = {1, 2, 3, 4, 5}
uset.symmetric_difference_update({2, 3, 9})
print(uset)
uset ^= {5, 9}
print(uset)
# Method "symmetric_difference_update" can also be applied to list, tuple, frozenset
ouset = {1, 2, 3, 4, 5}
uset = ouset
uset.symmetric_difference_update([2, 3, 9])
print(uset)
uset = ouset
uset.symmetric_difference_update((2, 3, 9))  # ???
print(uset)
uset = ouset
uset.symmetric_difference_update(frozenset([2, 3, 9]))
print(uset)

# Add another element
add = {1, 2, 3}
add.add(4)
print(add)

# Remove element
rmv = {1, 2, 3, 4, 5, 6, 7}
rmv.remove(5)
print(rmv)
# rmv.remove(99) => Exception: KeyError 99 not found

# Discard element (Remove if present, no exception)
dis = {1, 2, 3, 4, 5}
dis.discard(3)
print(dis)
dis.discard(9)
print(dis)

# Pop an arbitrary element
pop = {1, 2, 3}
pop.pop()
print(pop)
# {}.pop() => Exception; TypeError empty set

# clear every element in the set
rmv.clear()
print(rmv)
