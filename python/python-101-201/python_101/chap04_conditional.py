import math

if True:
    print("Do something")
else:
    print("Do something else")

if False:
    print("Don't do this")
elif True:
    print("Do something")
else:
    print("Do something else")

if True and False:
    print('yolo')
if True and True:
    print('yolo')
if True or False:
    print('yolo')
if False or False:
    print('yolo')
if (True and False) or not True:
    print('hm...')

x = "hello"
y = 'hello'
if x == y:
    print("String is matched")
else:
    print("String is not")

x = 123
y = 321
if x == y:
    print("Number is matched")
else:
    print("Number is not")

x = 0.33333333333
y = 1 / 3
if x != y:
    print("Float is not")
else:
    print("Float is matched")

if math.isclose(x, y):
    print("Float is closed")
else:
    print("Float is not closed")

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
if x == y:
    print("bang nhau zoi")
y.append(4)
if x != y:
    print("bang nhau deo")

x = (1, 2, 3)
y = (1, 2, 3)
if x == y:
    print("bang nhau lun")
y = (1, 3, 2)
if x != y:
    print("bang nhau beep")

x = {1, 2, 3}
y = {1, 2, 3}
if x == y:
    print("2 set y khoa")
y.add(5)
if x != y:
    print("2 set not y khoa")

x = {'1': 2, 1: '2'}
y = {'1': 2, 1: '2'}
if x == y:
    print("2 dict 1 cup")
y['1'] = 123
if x != y:
    print("2 dict 0 cup")

# Check for nothing
x = []
if not x:
    print("x is empty")

if __name__ == '__main__':
    print("Execute only when this file is run standalone")
