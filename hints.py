class Hints:

#dictonary
hints_dict = {
    1: "hint 1",
    2: "hint 2",
    3: "hint 3",
    4: "hint 4",
    5: "hint 5",
    6: "hint 6",
    7: "hint 7",
    8: "hint 8",
}
#used hints list
used_hints = []

#Question
print("Do you need a hint?")

# print(hints_dict.get(9, "There's no 9!"))

input("Y/N\n")
def get_hint(number):
    if len(used_hints) >= 3:
        print("Too Bad!")
        return
    hint = hints_dict.get(number)
    used_hints.append(number)
    return hint
