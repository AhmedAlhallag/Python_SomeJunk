"""
Evaluating addv2.py
"""
from subprocess import *
import sys

# a subprocess to open a pipe (adn execute) for the add.py script
# ====== without using the communicate method; using the stdout.read adn the stdin.write instaed
interpreter = sys.executable

# p1 = Popen([interpreter, "addv2.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
p2 = Popen([interpreter, "addv2.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

n1 = int(input(">> "))
n2 = int(input(">> "))
s = (n1+n2)
sqr = s ** 2
digits = len(str(sqr))
# p1.stdin.write(bytes(f"{n1}\n{n2}\n{(n1+n2)**2}\n", "UTF-8"))
p2.stdin.write(bytes(f"{n1}\n{n2}\n", "UTF-8"))
# stdout = p1.stdout.read().decode("UTF-8")
# stdout = p1.stdout.readline()
# p1.stdin.close()
p2.stdin.close()

print(p2.stdout.read().decode("UTF-8"))
print(p2.stderr.read().decode("UTF-8"))

# print(stdout)


# for i in range(8):
#     print(p1.stdout.readline())

# print(p1.stdout.read())


# lines = open("addv2.py", "r").readlines()
# for i in range(len(lines)):
#     print(lines[i])
#     if lines[i].find("input(") > -1:
#         print(f"previous line is: {lines[i-1]}")
#         # print("Last character in that previous line: ")
#         lschar = lines[i-1][len(lines[i-1])-1:]


# end = False
# while not end:
#     line = p1.stdout.readline()
#     print(line.decode("UTF-8"))
#     pattern = b"EOF\n"
#     endIdx = line.find(pattern)
#     if endIdx > -1:
#         end = True

# search for input
# this will not work if your'e parsing the stdout (which includes on print statement)
# + that you need to feed the inputs to the py file your'e running at the point when you start piping into the file being ran as a subprocess
# input_pattern = b"Enter"
# inputIdx = line.find(input_pattern)
# if inputIdx > -1:
#     print("Found an input!")


# bar = "+"+"-"*50 + "+"

# notFound = True
# while (notFound):

#     line = p2.stdout.readline()
#     print(line.decode("UTF-8"))
#     # str_line = line.decode("UTF-8")
#     exitingpattern = b"EOF\n"
#     idx2 = line.find(exitingpattern)

#     if idx2 > -1:
#         print("No mtches found")
#         break

#     exp1 = f"{sqr}\n"
#     pattern_exp1 = eval(exp1)
#     exp2 = f'b"{pattern_exp1}"'
#     pattern_exp2 = eval(exp2)
#     # print("pattern in bytes:", pattern_exp2)
#     # pattern2 = b"\nSum is"

#     # print("pattern:", exp1)

#     idx = line.find(pattern_exp2)
#     if idx > -1:
#         # print("index:", idx)
#         # print("no. of digits", digits)
#         print(bar)
#         print(line[idx:idx+digits])
#         print("Found it")
#         print(bar)

#         n_str = line[idx:idx+digits].decode("UTF-8")
#         # if n_str == "25":
#         # pass
#         # p1.stdin.write(bytes("yes\n", "UTF-8"))

#         notFound = False


# stderr = p1.stderr.read().decode("UTF-8")

# print(stdout)
# print(stderr)
# if stdout.find("15"):
#     print("WOW")
