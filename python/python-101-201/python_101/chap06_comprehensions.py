# List Comprehensions
x = [1, 2, 3, 4, 5]
y = [num * num for num in x]
"""
y = []
for num in x:
    y.append(num * num)
"""
print(y)
x = ['1', '2', '3', '4', '5']
y = [int(num) * 3 for num in x]
"""
y = []
for num in x:
    y.append(int(num) * 3)
"""
print(y)
z = [(x, y) for x in [1, 2, 3] for y in [1, 5, 6] if x != y]
"""
y = []
for x in [1, 2, 3]:
    for y in [1, 5, 6]:
        if x != y:
            z.append((x, y))
"""
print(z)
z = [squr for row in [[1, 2, 3], [4, 5, 6], [6, 7]] for squr in row]
"""
z = []
for row in [[1, 2, 3], [4, 5, 6], [6, 7]]:
    for squr in row:
        z.append(squr)
"""
print(z)


# Dictionary Comprehensions
x = [1, 2, 3, 4, 5]
y = {num: str(num) for num in x}
"""
y = {}
for num in x:
    y[num] = str[num]
"""
print(y)
# Reverse key and value
y = {value: key for key, value in y.items()}
print(y)

# Set Comprehensions (same as list but using {})
y = {value for value in x}
print(y)
