from subprocess import Popen, PIPE, STDOUT
import pty
import os
import sys

interpreter = sys.executable

cmd = [interpreter, "addv2.py"]

master, slave = pty.openpty()

# tokenizer = Popen(cmd, stdin=PIPE, stdout=slave)

p = Popen(cmd, shell=True, stdin=PIPE, stdout=slave, close_fds=True)
stdin_handle = p.stdin
stdin_handle.write(bytes("2\n2\nyes\n", "UTF-8"))
stdin_handle.close()
stdout_handle = os.fdopen(master)

print(stdout_handle.readline())
# print(stdout.readline())
