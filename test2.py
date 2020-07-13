import re
dict1 = {
    1: "choco",
    2: "choc",
    3: "chocolat"

}

# print(dict1[4])
with open("choc.txt", "r+") as originalFile:
    # Note: What I'm doing is:
    # reading all lines as a list of elements,
    # I can either join them (over new line) to form one string
    # and itertae over each line (elem)
    # to find  adn replace the desired word
    # OR: Like domic's sol:
    # no jeat "read()" as one text; this no need for a loop

    data = originalFile.readlines()

    print(data)
    print(len(data))

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

    # for line in data:
    #     print(line)
    #     line2 = line.lower()
# original_reduced = re.sub("[^a-zA-Z0-9]", " ", str)
    print(data[0])

    print(re.sub("[^a-zA-Z0-9\s | (\.*,':!?)]", " ", data[0]))

    print(data[1])

    print(re.sub("[^a-zA-Z0-9\s | (\.*,':!\?)]", " ", data[1]))

    print(data[2])

    print(re.sub("[^a-zA-Z0-9\s | (\.*,':!\?)]", " ", data[2]))

    print(data[3])

    print(re.sub("[^a-zA-Z0-9\s | (\.*,':!\?)]", " ", data[3]))

    print(data[4])

    print(re.sub("[^a-zA-Z0-9\s | (\.*,':!\?)]", " ", data[4]))
