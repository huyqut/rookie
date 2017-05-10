# LOOP

# RANGE

# Initialize a range with exclusive stop only (default: start = 0, step = 1)
print(list(range(10)))

# Initialize a range with inclusive start and exclusive stop (default: step = 1)
print(list(range(1, 10)))

# Initialize a range with inclusive start, exclusive stop and # of steps
print(list(range(1, 10, 3)))

# Applied to negative number
print(list(range(1, -10, -1)))

# Empty range if stop >= start
print(list(range(1, 1)))
print(list(range(2, 1)))

# FOR

# Use with range
for num in range(10):
    print(num, end = ' ')
print()
for num in range(1, 10, 3):
    print(num, end = ' ')
print()
for num in range(1, -10, -2):
    print(num, end = ' ')
print()

# Use with list
misclist = [1, '2', (3, 4)]
for element in misclist:
    print(element, end = ' ')
print()

# Use with tuple
misctuple = (1, '2', [3, 4])
for element in misctuple:
    print(element, end = ' ')
print()

# Use with set
miscset = {1, '2', (3, 4)}
for element in misctuple:
    print(element, end = ' ')
print()

# Use with dict (all following methods generate view objects and update realtime)
miscdict = {1: '1', '2': 2, (3, 4): [4, 5]}
for key in miscdict:
    print(key, end = ' ')
print()
for key in miscdict.keys():
    print(key, end = ' ')
print()
for value in miscdict.values():
    print(value, end = ' ')
print()
for element in miscdict.items():
    print(element, end = ' ')

# WHILE loop
while True:
    x = input('x = ')
    if x == 'x':
        break
    else:
        continue
