import random
import re


def srch_and_replace_chocolate(str, replacement):
    str = str.lower()
    original_reduced = re.sub("[^a-zA-Z0-9\s]", "", str)
    # original_reduced = re.sub("[ ^ a-zA-Z0-9\s | (\., ':!\?)]", "", str)

    subbed = re.sub("chocolate", replacement, original_reduced)
    flag = (subbed != original_reduced)
    if flag:
        return subbed
    return flag


def srch_and_replace_chocolate_v3(str, replacement):
    # str = str.lower()
    # original_reduced = re.sub("[^a-zA-Z0-9]", " ", str)
    original_reduced = re.sub("[^a-zA-Z0-9 | (.*,':!?)]", " ", str)

    word = ["c", "h", "o", "c", "o", "l", "a", "t", "e"]
    list_of_tuples = []
    # print(original_reduced)
    for currIDX in range(0, len(original_reduced)):
        # currIDX = x
        nextIDX = currIDX + 1
        if nextIDX == len(original_reduced):
            break

        # print("Current Character: ", original_reduced[currIDX])
        if original_reduced[currIDX].lower() == "c":
            i = 1
            count = 1
            while nextIDX < len(original_reduced):

                if (original_reduced[nextIDX].lower() == "c") and (count == 1):
                    # currIDX = nextIDX - 2
                    break
                if original_reduced[nextIDX].lower() == word[i]:
                    # print(">>", original_reduced[nextIDX], end=" ")
                    # print(list_of_tuples)

                    count += 1
                    nextIDX += 1
                    i += 1
                else:
                    if original_reduced[nextIDX] == " ":
                        nextIDX += 1
                        continue
                    else:
                        break
                    # print(original_reduced[nextIDX])
                    # # break
                    # skips += 1
                    # continue

                if count == 9:
                    finIDX = nextIDX - 1
                    list_of_tuples.append((currIDX, finIDX))
                    break
    # print(len(original_reduced))
    # print(original_reduced)
    # print("BEFORE:    ", list_of_tuples)

    for elem in list_of_tuples:
        # print(elem)
        i = 1
        index = list_of_tuples.index(elem)
        list_of_tuples[index] = original_reduced[elem[0]:elem[1]+1]
        # exp = f'substr{i} = "{list_of_tuples[index]}"'
        # i += 1
        # eval(exp)
    preFinalExp = ""
    for i in range(len(list_of_tuples)):
        substrLen = len(list_of_tuples[i])
        # tempExp = f'.replace("{list_of_tuples[i]}", "+"*{substrLen})'
        tempExp = f'.replace("{list_of_tuples[i]}", "{replacement}".center({substrLen},"+") )'
        preFinalExp = preFinalExp + tempExp

    finalExp = f'"{original_reduced}"{preFinalExp}'
    subbed = eval(finalExp)
    # bar = "+" + "-"*50 + "+"

    # print("From inside the function")
    # print(bar)

    # print(subbed)
    # print("AFTER:   ", list_of_tuples)

    return subbed


def generateAFile(inputFileName):
    fileName = random.choice(["choco.txt", "choc.txt", "chocolat.txt"])
    replace = random.choice(["carrot", "cocoa", "cream"])
    lines = ["Chocolate, CHOCOLATE : you're the best!",
             "Milk chocolate, dark chocolate?  Who cares?",
             "I'm happy when I eat chocolate.  You?",
             "This line does not contain c-h-o-c-o-l-a-t-e",
             "It's cold... I want some hot chocolate, now!"]
    title = ["POEM: Chocolate Poem",
             "POEM: Chocolate Chocolate", "POEM: Chocolate Anyone?"]
    author = ["--Anonymous", "--Francis", "--DFT"]

    poem = [random.choice(title),
            random.choice(lines),
            random.choice(lines),
            random.choice(lines),
            random.choice(author)]
    poem = "\n".join(poem)
    text = poem + "\n"
    # print(text)
    # print(fileName)
    # print(replace)
    file = open(fileName, "w")
    file.write(text)
    file.close()

    file = open(inputFileName, "w")
    file.write(fileName + "\n")

    file.write(replace + "\n")

    file.close()

    return text, fileName


text, fileName = generateAFile("AnyFile.txt")

names = ["choco.txt", "choc.txt", "chocolat.txt"]

# print(fileName)

print(f"""
      One of the following files is already generated randomly,
      1. choco.txt
      2. choc.txt
      3. chocolat.txt
      -> The generated file is {fileName}.
      :Enter the number of the generated file as an input
      """)

dict1 = {
    1: "choco.txt",
    2: "choc.txt",
    3: "chocolat.txt"
}

while(1):
    try:
        fileNumber = int(input(">> "))
        if (3 >= fileNumber >= 1):
            inputfilename = dict1[fileNumber]
            break
        else:
            print("Pick a number that correspnds to a file name from the list please")

    except:
        print("Enter only Digits please.")


replacement = input("What word would you want to replace 'chocolate' by? ")
with open(inputfilename, "r+") as originalFile:
    # Note: What I'm doing is:
    # reading all lines as a list of elements,
    # I can either join them (over new line) to form one string
    # and itertae over each line (elem)
    # to find  adn replace the desired word
    # OR: Like domic's sol:
    # no jeat "read()" as one text; this no need for a loop

    data = originalFile.readlines()

    # print(data)

    new_text = ""

    # +--------EAsy Solution---------+
    # for line in data:
    #     new_line = line.replace("Chocolate", replacement.capitalize()).replace(
    #         "CHOCOLATE", replacement.upper()).replace(
    #             "chocolate", replacement.lower())
    #     ret = srch_and_replace_chocolate(new_line, replacement)
    #     if ret:
    #         new_text = new_text + ret
    #     else:
    #         new_text = new_text + new_line
    # print(data)

    for line in data[:-1]:
        new_line = line.replace("Chocolate", replacement.capitalize()).replace(
            "CHOCOLATE", replacement.upper()).replace(
                "chocolate", replacement.lower())
        ret = srch_and_replace_chocolate_v3(new_line, replacement)
        if ret:
            new_text = new_text + ret + "\n\n"
        else:
            new_text = new_text + new_line + "\n\n"

bar = "+" + "-"*50 + "+"
print("\n"+bar)

print("+"+"-"*19+"Original Text"+"-"*18+"+")
print(bar+"\n")
print("\n".join(data))
new_lines = new_text.strip().split("\n")
# printing the title in uppercase
print(bar)
print("+"+"-"*19+"Replaced Text"+"-"*18+"+")
print(bar+"\n")

print(new_lines[0].upper())

# loop to print the rest of the lines

for line in new_lines[1:]:
    print(line)

print("\n"+data[-1]+"\n")


print(bar)
print("+"+"-"*15+"File Writing Status"+"-"*15+"+")
print(bar)
print("+"+"-"*15+"Written Successfully"+"-"*15+"+")
print(bar+"\n")

with open("user_output.txt", "w") as of:
    of.write(new_lines[0].upper()+"\n")
    print(new_lines[0])
    for line in new_lines[1:]:
        of.write(line+"\n")
        print(line)
    of.write("\n"+data[-1]+"\n")
    print("\n"+data[-1])


# print(new_text)
# print(new_lines)


# tetsing find function

# string = "my name is Ahmed with a capital AyoAHole! got it memorized?"

# index = string.find("AyoAHole")


# print(index)
