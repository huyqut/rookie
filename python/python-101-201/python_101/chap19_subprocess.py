# Subprocess

import subprocess

# Call without arguments
subprocess.call('ls')  # Call a binary
# Call with arguments
subprocess.call(['code', '--version'])

# Execute a child program in a new process (does NOT wait)
subprocess.Popen('ls')
print('yolo')

# Communications
ping = subprocess.Popen(['ping', 'www.google.com'], stdout = subprocess.PIPE)

data = ping.communicate()
for line in data:
    print(line)
