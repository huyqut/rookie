# Initialize a string
single_quote = 'English'
print(single_quote)

double_quote = "This is Python!"
print(double_quote)

triple_quote = '''This
    Is
  Sparta'''
print(triple_quote)

# Length of a string
print(len(single_quote))
print(len(double_quote))
print(len(triple_quote))

# Concatenate strings
print(single_quote + double_quote)
print('3' + triple_quote + '2')

# Repeat strings
repstr = 3 * double_quote
print(repstr)

# String <=> Number
num = 123456
numstr = str(num)
print(numstr)
numstr = '1' + numstr + '2'
num = int(numstr)
print(num)

# String <=> Float
flt = 123.456
fltstr = str(flt)
print(fltstr)
fltstr = '2' + fltstr + '1'
flt = float(fltstr)
print(flt)

# String normalization methods
up = "this is sparta".upper()
print(up)
low = "THIS IS SPARTA".lower()
print(low)
cap = "tHIS IS SPARTA".capitalize()
print(cap)
title = "tHIS iS sPARTA".title()
print(title)
swapcase = "tHiS iS sPaRtA".swapcase()
print(swapcase)
center = "this is sparta".center(30, '|')
print(center)
left_align = "    this is sparta  ".ljust(30, '|')
print(left_align)
right_align = "   this is sparta  ".rjust(30, '|')
print(right_align)
left_strip = "    this is sparta  ".lstrip()
print(left_strip)
left_strip = "|||||this is sparta||||".lstrip('|')
print(left_strip)
right_strip = "   this is sparta    ".rstrip()
print(right_strip)
right_strip = "    this is sparta||||".rstrip('|')
print(right_strip)
print("42".zfill(5))
print("-42".zfill(10))

# String Slices (0-based index, begin inclusive, end exclusive)
message = "This is sparta"
print(message[3])
sub = message[3:7]
print(sub)
sub = message[:7]
print(sub)
sub = message[3:]
print(sub)
sub = message[8:-3] # 3 letters before
print(sub)
sub = message[:-5] # 5 letters before
print(sub)

# String format
print("{0} + {1} = {2}".format(3, 9, 3 + 9))
print("{1} + {0} = {2}".format(3, 9, 3 + 9))
print(f"{num} and {flt} are friends")

# String properties
print("abc".isalpha())  # True
print("ab2".isalpha())  # False
print("123".isnumeric())  # True
print("a23".isnumeric())  # False
print("a1b".isalnum())  # True
print("a1".isalnum())  # False
print("123".isdecimal())  # True
print("123.321".isdecimal())  # False
print("    ".isspace())  # True
print("  a ".isspace())  # False
print("This Is Sparta".istitle())  # True
print("this Is Sparta".istitle())  # False
print("THIS IS SPARTA".isupper())  # True
print("ThIS IS SPARTA".isupper())  # False
print("this is sparta".islower())  # True
print("this iS sparta".islower())  # False

# String matching
print(repstr.count("This is Python!"))  # 3
print("Doctor who".endswith("who"))  # true
print("Doctor who ".endswith("who"))  # False
print("Doctor who".startswith("Doctor"))  # True
print(" Doctor who".startswith("Doctor"))  # False
haystack = "yolo lolo yolo lolo"
print("yolo" in haystack)  # True
print("yoyo" in haystack)  # False
print(haystack.find("lolo"))  # 5
print(haystack.find("lolo", 0, 3))  # -1

# String partitions
print("x y y z".partition('y'))
print("x y y z".partition('k'))
print("x y y z".rpartition('y'))
print("x y y z".rpartition('h'))
print("x y z".split(' '))
print("x,y,z".split(',', maxsplit = 1))
print("x y z".rsplit(' '))
print("x,y,z".rsplit(',', maxsplit = 1))
print("x\ny\nz".splitlines())
print("xy\r\nyz\r\nzk".splitlines())
