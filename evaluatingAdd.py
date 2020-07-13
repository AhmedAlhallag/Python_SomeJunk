"""
Evaluating add.py
"""
from subprocess import *
import sys


# a subprocess to open a pipe (adn execute) for the add.py script
# ====== without using the communicate method; using the stdout.read adn the stdin.write instaed
interpreter = sys.executable

p1 = Popen([interpreter, "add.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

p1.stdin.write(bytes("12\n3\n", "UTF-8"))

# data = p1.communicate(input=bytes("12\n3\n", "UTF-8"))[0].decode("UTF-8")

# NOt necessary if the comminicate method was used; it closes files' streams by default
p1.stdin.close()

# print(p1.stdout.read().decode("UTF-8"))
stdout = p1.stdout.read().decode("UTF-8")


print(stdout)
if stdout.find("15"):
    print("WOW")


# Alternativly: using p1.communicate

# print(data)
# if data.find("15"):
#     print("WOW")
# print(data[0].decode("UTF-8"))
