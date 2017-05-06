# FILES

# Get all data
handle = open('/Users/huyqut/Documents/hello_py', 'r')
data = handle.read()
print(data)
handle.close()

# Get line by line (empty string if reached end of file)
handle = open('/Users/huyqut/Documents/hello_py', 'r')
data = handle.readline()
print(data)
handle.close()

# Get all lines (including end of line)
handle = open('/Users/huyqut/Documents/hello_py', 'r')
data = handle.readlines()
print(data)
handle.close()

# Process line by line using for
handle = open('/Users/huyqut/Documents/hello_py', 'r')
for line in handle:
    print('yolo = ' + line)
handle.close()

# Process by a chunk of bytes
handle = open('/Users/huyqut/Documents/hello_py', 'r')
while True:
    data = handle.read(12)
    if not data:
        break
    print(data)
handle.close()

# Process binary files: use "rb" mode
handle = open('/Users/huyqut/Documents/hello_py', 'rb')
handle.seek(5)  # Go to 6th byte from beginning
handle.seek(5, 0)  # The same as above
print(handle.read(1))  # After reading a chunk of bytes, cursor auto jumps to the next one
handle.seek(5, 1)  # Go to the 5th byte from current position
print(handle.read(1))
handle.seek(-3, 2)  # Go to 3 previous bytes from the end position
print(handle.read(1))
handle.close()


# Write a file in text mode (r) or binary mode (rb)
# If the file does not exist, a new file is created.
# If the file already exists, the old file is replaced without warning.

handle_text = open('/Users/huyqut/Documents/hello_pi', 'w')
handle_text.write('Sup yo???')
handle_text.close()
handle_bin = open('/Users/huyqut/Documents/hello_bi', 'wb')
handle_bin.write(b'yolo')
handle_bin.close()

# "with" operator: auto-close file and reduce the scope of the file
with open('/Users/huyqut/Documents/hello_py', 'r') as handle:
    print(handle.read())
