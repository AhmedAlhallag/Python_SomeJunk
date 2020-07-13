from subprocess import *

with open("out_list.txt", "r") as file:
    pipedData = file.read()
    bytess = eval(pipedData)
    p2 = run(["grep", "-in", "test"], stdout=PIPE,
             input=bytess)
    print(p2.stdout.decode())
