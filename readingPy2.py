lines = open("habal.py", "r").readlines()
for i in range(len(lines)):
    print(lines[i])
    if lines[i].find("input(") > -1:
        print(f"previous line is: {lines[i-1]}")
        # print("Last character in that previous line: ")
        lschar = lines[i-1][len(lines[i-1])-1:]
        if lschar == "\n":
            print("Found the last character which is a newline")
