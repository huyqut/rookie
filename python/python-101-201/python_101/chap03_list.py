# LIST (Mutable Sequence)

# Empty list
empty_list_sqr = []
empty_list_obj = list()

# List of numbers
numlist = [3, 2, 1]
print(numlist)

# List of strings
strlist = ['a', "b", '''c''']
print(strlist)

# List of misc
misclist = [1, "a", 3.4]
print(misclist)

# List slices
print(misclist[0])
print(misclist[1])
print(misclist[2])
print(misclist[:3])
print(misclist[1:])
print(misclist[1:3])
print([1, 2, 3, 4, 5][3:-1])
print([1, 2, 3, 4, 5][::2])
temp = ['x', 'w', 'h']
temp[0] = 'y'
print(temp)

# Nested list
nested_list = [numlist, strlist]
print(nested_list)

# Extend a list
misclist.extend(strlist)
print(misclist)

# Concatenation of 2 lists
concat = numlist + strlist
print(concat)

# Append an element
misclist.append('1')
print(misclist)

# Pop out an element (Default -1 = the end)
misclist.pop(3)
print(misclist)
misclist.pop()
print(misclist)

# Check if an element is in list
print(3.4 in misclist)  # True
print("4.3" in misclist)  # False
print(3.4 not in misclist)  # False
print("4.3" not in misclist)  # True

# Length of a list
print(len(misclist))

# In-place Sort a list (all elements in the list must be 1 type)
numlist.sort()
print(numlist)
strlist.sort(reverse = True)
print(strlist)

# Minimum of a list (all elements in the list must be 1 type)
print(min(numlist))
print(min(strlist))

# Maximum of a list (all elements in the list must be 1 type)
print(max(numlist))
print(max(strlist))

# Find index of an element
print(numlist.index(1))
# print(numlist.index(1, 2, 3)) => Exception

# Repeat a list
thrice = numlist * 3
print(thrice)

# Count # of occurences
print(thrice.count(1))

# Reverse elements
strlist.reverse()
print(strlist)

# Replace a portion of a list
thrice[1:4] = [1, 2, 3, 4, 5]
print(thrice)

# Insert an element to a list
thrice.insert(5, 100)
print(thrice)

# Remove 1st item that matches
rem = [1, 2, 1, 3]
rem.remove(1)
print(rem)

# Remove middle elements (in-place)
del thrice[2:5]
print(thrice)
thrice[5:6] = []
print(thrice)

# Empty the list
thrice.clear()
print(thrice)
