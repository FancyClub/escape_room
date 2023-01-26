# create class
class Hints:

    def __init__(self, max_hints=3):

        # dictonary
        self.hints_dict = {
            1: "hint 1",
            2: "hint 2",
            3: "hint 3",
            4: "hint 4",
            5: "hint 5",
            6: "hint 6",
            7: "hint 7",
            8: "hint 8",
        }

        self.used_hints_dict = {
            1: "1st",
            2: "2nd",
            3: "last",
        }

        # used hints list
        self.used_hints_list = []

        self.max_hints = max_hints
        self.used_hints_number = 0


    def get_hint(self, number):

        if self.used_hints_number >= self.max_hints:
            print("Too Bad! You've used all 3 of your hints")
            return

        user_input = input(f"""
            Are you sure you would like to use your {self.used_hints_dict} of {self.max_hints}? [Y/N]
        """)

        if user_input.upper() != "Y":
            return

        self.used_hints_list.append(number)

        return self.hints_dict.get(number)
