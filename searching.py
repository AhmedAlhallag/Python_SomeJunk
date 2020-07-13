import re


def srch(str):

    str2_new = str.lower()

    new = re.sub("[^a-zA-Z0-9\s]", "", str2_new)

    # re.match()
    print(new)

    new2 = re.sub("chocolate", " +-----+ ", new)

    print(new2)

    new3 = re.sub("chocolate", "  __chocolate__  ", new)

    print("NEW2 CONTENT: ", new3)

    pattern = re.compile(r"chocolate")

    matches = pattern.finditer(new)

    indices = []

    for match in matches:
        print(match)
        indices.append(tuple(list(match.span())))

    print(indices)
    if indices:
        print(f"Found {len(indices)} matches of 'chocolate'!")
        print("String before special characters removal: ")
        print(str2)
        print("String AFTER special characters removal and lowercasing: ")
        print(new)
        print("+"+"-"*30+"+")
        print("[Clarification1] Position(s) of matches: ")
        print(new3)
        print("[Clarification2] Position(s) of matches: ")
        print(new2)
    else:
        print("no matches found!")


def srch_and_replace_chocolate(str, replacement):
    str = str.lower()
    original_reduced = re.sub("[^a-zA-Z0-9]", " ", str)
    word = ["c", "h", "o", "c", "o", "l", "a", "t", "e"]
    list_of_tuples = []
    for char in original_reduced:
        if char == "c":
            i = 1
            count = 1
            currIDX = original_reduced.index(char)
            nextIDX = currIDX + 1
            while(nextIDX <= len(original_reduced)-1):
                if count == 9:
                    finIDX = nextIDX - 1
                    list_of_tuples.append(tuple(currIDX, finIDX))
                    break
                if original_reduced[nextIDX] == word[i]:
                    count += 1
                    nextIDX += 1
                    i += 1
                else:
                    nextIDX += 1

    # subbed = re.sub("chocolate", replacement, original_reduced)
    # flag = (subbed != original_reduced)
    # if flag:
    #     return subbed
    # return flag
    return list_of_tuples


rep = "nadine"


def srch_and_replace_chocolate_v2(str, replacement):
    # str =
    # str2 = str.lower()
    original_reduced = re.sub("[^a-zA-Z0-9]", " ", str)
    word = ["c", "h", "o", "c", "o", "l", "a", "t", "e"]
    list_of_tuples = []
    print(original_reduced)
    for currIDX in range(0, len(original_reduced)):
        # currIDX = x
        nextIDX = currIDX + 1
        if nextIDX == len(original_reduced):
            break

        print("Current Character: ", original_reduced[currIDX])
        if original_reduced[currIDX].lower() == "c":
            i = 1
            count = 1
            while((nextIDX < len(original_reduced))):

                if (original_reduced[nextIDX].lower() == "c") and (count == 1):
                    # currIDX = nextIDX - 2
                    break
                if original_reduced[nextIDX].lower() == word[i]:
                    print(">>", original_reduced[nextIDX], end=" ")
                    print(list_of_tuples)

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
    print(len(original_reduced))
    print(original_reduced)
    print("BEFORE:    ", list_of_tuples)

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
        tempExp = f'.replace("{list_of_tuples[i]}", "{rep}".center({substrLen},"+") )'
        preFinalExp = preFinalExp + tempExp

    finalExp = f'"{original_reduced}"{preFinalExp}'
    subbed = eval(finalExp)
    print(subbed)
    print("AFTER:   ", list_of_tuples)

    return list_of_tuples, original_reduced, subbed


def srch_and_replace_chocolate_v3(str, replacement):
    # str = str.lower()
    original_reduced = re.sub("[^a-zA-Z0-9]", " ", str)
    word = ["c", "h", "o", "c", "o", "l", "a", "t", "e"]
    list_of_tuples = []
    # print(original_reduced)
    for currIDX in range(0, len(original_reduced)):
        # currIDX = x
        nextIDX = currIDX + 1
        if nextIDX == len(original_reduced):
            break

        # print("Current Character: ", original_reduced[currIDX])
        if original_reduced[currIDX] == "c":
            i = 1
            count = 1
            while((nextIDX < len(original_reduced))):

                if (original_reduced[nextIDX] == "c") and (count == 1):
                    # currIDX = nextIDX - 2
                    break
                if original_reduced[nextIDX] == word[i]:
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
        tempExp = f'.replace("{list_of_tuples[i]}", "{rep}".center({substrLen},"+") )'
        preFinalExp = preFinalExp + tempExp

    finalExp = f'"{original_reduced}"{preFinalExp}'
    subbed = eval(finalExp)
    # print(subbed)
    # print("AFTER:   ", list_of_tuples)

    return subbed


str = "Chocolate! This file does not contain c-h-o-c-o-l-a-t-e chari, c-h-a-s-i-s cholo c-h-o-l-o-l-o-l-o"

str2 = "Chocolate! This file does not contain C%h__=_=o_c-o.l,,a..t-*\e c-h-o-c-o-l-a-t-e c-jkbkhbjhbh-o-c-o-l-a-t-e  chari, c-h-a-s-i-s cholo c-h-o-l-o-l-o-l-o"


# m = re.match(pattern, new)

# m2 = m.groupdict()
# m3 = list(matches)

# print(m)
# print(m3)
str3 = "This line does not contain c-h-o-c-o-l-a-t-e"
# srch(str3)

l, o, r = srch_and_replace_chocolate_v2(str2, "milk")

print(l)

print(o[0:9])
# print(o[3:63])
print(o[38:63])
print(o[64:81])
bar = "+" + "-"*50 + "+"
print(bar)
print(str2)
bar = "+" + "-"*50 + "+"
print(bar)
print(r)
# print(o[82:108])


# print(srch_and_replace_chocolate(str2, "milk"))

# print(str3[19:44])
# print(str3[27:44])
