import os
import pty
import subprocess
import sys

interpreter = sys.executable


master, slave = pty.openpty()
process = subprocess.Popen([interpreter, "addv2.py"], stdout=slave,
                           stdin=slave, stderr=slave, close_fds=True)

# os.close(slave)


# os.read(master, 1024).decode("UTF-8")

output = []
while True:
    try:
        data = os.read(master, 1024)
        if len(data) == 0:
            break

    except OSError:
        break
    if not data:
        break
    output.append(data)  # In Python 3, append ".decode()" to os.read()
output = "".join(output)
