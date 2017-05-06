# List Comprehensions
x = [1, 2, 3, 4, 5]
y = [num * num for num in x]
print(y)
x = ['1', '2', '3', '4', '5']
y = [int(num) * 3 for num in x]
print(y)
y = [(x, y) for x in [1, 2, 3] for y in [1, 5, 6] if x != y]
print(y)

# Nested List Comprehensions


# Dictionary Comprehensions

