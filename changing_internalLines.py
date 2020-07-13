# with open("user_output.txt","r") as file:

fnName = "Hamada"
i = 1
with open("pyt1_edited.py", "w") as edited:
    for line in open("pyt1.py", "r").readlines():
        comIDX = line.find("#")
        if comIDX >= 0:
            # we found a comment; remove it
            print(f"Found a Comment:x{i}")
            i += 1
        else:
            edited.write(line)
