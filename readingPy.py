from subprocess import *

# cp = run("ls -la | grep -i test", capture_output=True, shell=True)
# cp2 = Popen("ls -la | grep -i test", stdout=PIPE, shell=True)


newFileName = "nhabal2" + ".txt"
pushing = Popen(f"cat habal.py > {newFileName}", shell=True)

# print(cp2.stdout.read())
# print(pushing.stdout.read())


data = open(newFileName, "r").read()
print(data)

inputIdx = data.find("input(")
# if inputIdx > -1:
#     # get the previos indeices..

#     while True:
#         match = data[prevIdx:prevId]
#         print(match)
#         prevIdx = inputIdx-i
#         i += 2

# newlineIdx = data.find("\n")
# print(newlineIdx)
# print(data[newlineIdx:newlineIdx+1])

# print("Found an input!")
# print("Previous index:", prevIdx)
# print(data[prevIdx:prevIdx+1])
