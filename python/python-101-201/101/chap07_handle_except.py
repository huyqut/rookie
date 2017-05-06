# EXCEPTION HANDLING

# Handle any exception
try:
    print("fine")
except:
    print("Any exception raised is solved here")

# 1-1 Handling exception
try:
    1 / 0
except ZeroDivisionError:
    print("Division by Zero")
print("Done")

# Many 1-1 Handling exception
my_dict = {'1': 1, 1: '1'}
try:
    index = input('index = ')
    value = my_dict[index]
except IndexError:
    print('Index Error here')
except KeyError:
    print('Key Error here')
except:  # anything else
    print('yolo')

# Get exception object
try:
    1 / 0
except ZeroDivisionError as e:
    print(str(e))

# Many-1 Handling exception
try:
    index = input('index = ')
    value = my_dict[index]
except (IndexError, KeyError) as e:
    print('Those 2 are the same: ' + str(e))

# "finally" in exception (ALWAYS run in either except or no except)
try:
    value = my_dict[2]
except KeyError:
    print('This is so wrong')
finally:
    print('Finish him!!!')

# "else" in exception (when NO exception is raised, then it is run)
try:
    value = my_dict[1]
except KeyError:
    print("Should not happen")
else:
    print("Everything is fine? OK. I'm out")
