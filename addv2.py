"""
Adding two number from the user
"""


def check_secret_squared(n):
    secret_sqr = 25
    return (n*n) == secret_sqr


n1 = int(input("\nEnter the first number: "))
n2 = int(input("\nEnter the 2nd number: "))
n3 = int(input("\nEnter the 2nd number: "))

s = n1+n2
print("\nSum is: ", s)

# rep = input("\nAre we done? (yes/no)>> ")
# print(rep)

# if rep == "yes":
#     print("\nOK BYE!")
# else:
#     print("\nUnkown input. BYE!")

# rep = int(input("\nPlease Enter the square of that sum: "))

print("\nCalculating sqr...")
print("\nSquare:", s*s)
print("\nIs this our secret squared number... ?")

# ans = input("(yes/no)>> ")

# if check_secret_squared(s) and ans == "yes":
#     print("\nIT IS! Buddies For Life! Seems like your sum was = 5")
# else:
#     print("\nI guess you do not remember after all..")


# print("\nEOF")
