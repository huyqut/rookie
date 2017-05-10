# The os module (Operating System related functions)

import os
import shutil

# 1. Process parameters

print(os.name)  # Name of current os
print(os.ctermid())  # Filename of terminalR
print(os.environ)  # A dict of global environments of the system
print(os.getenv('PATH'))  # Get an environment variable
print(os.putenv('CHAP16', "OS Modules"))  # Set an environment variable
print(os.getlogin())  # Get current login of terminal
print(os.getpid())  # Get current process id

# 2. File descriptors (to be continued...)

# 3. File and Directories
print(os.getcwd())  # Get current working directory
print(os.chdir('..'))  # Change directory
print(os.mkdir('chap16'))  # Make a new directory
print(os.makedirs('chap16/wolo/yolo/wala'))  # Make a new directory (with intermediate folders if not existed)
#print(os.rmdir('A file'))  # Remove a file
#print(os.rmdir('chap16'))  # Remove a directory (must be empty)
shutil.rmtree('chap16')  # Remove a directory and its children
# os.rename('from', 'to')  # Rename a file (can be used to move a file)
for root, dirs, files in os.walk('.'):
    print(root)

print(os.path.basename('./python_101/chap16_os.py'))  # File name of a path
print(os.path.dirname('./python_101/chap16_os.py'))  # Enclosing directory of a path of the file name
print(os.path.exists('./python_303'))  # Check if a directory exists
print(os.path.isdir('./python_101'))  # Check if a path is a directory
print(os.path.isfile('./python_101/chap16_os.py'))  # Check if a path is a file
print(os.path.split('./python_101/chap16_os.py'))  # Split dir and base name part into a pair
