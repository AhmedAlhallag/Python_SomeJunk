"""
Evaluating addv2.py
"""
from subprocess import *
import sys

interpreter = sys.executable

p1 = Popen([interpreter, "addv2.py"], stdout=PIPE, stdin=PIPE)

# n1 = int(input(">> "))
# n2 = int(input(">> "))
n1 = 2
n2 = 3
p1.stdin.write(f"{n1}\n{n2}\n")

p1.stdin.close()


while p1.poll() is None:
    output = p1.stdout.readline()
    sys.stdout.write(output.decode("UTF-8"))
    sys.stdout.flush()
# s = (n1+n2)
# sqr = s ** 2
# digits = len(str(sqr))


# print(p1.stdout.read().decode("UTF-8"))
