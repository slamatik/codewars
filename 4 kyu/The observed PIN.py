def get_pins(observed):
    data = {"1": ["1", "2", "4"],
            "2": ["1", "2", "3", "5"],
            "3": ["2", "3", "6"],
            "4": ["1", "4", "5", "7"],
            "5": ["2", "4", "5", "6", "8"],
            "6": ["3", "5", "6", "9"],
            "7": ["4", "7", "8"],
            "8": ["5", "7", "8", "9", "0"],
            "9": ["6", "8", "9"],
            "0": ["0", "8"]}
    n = len(observed)
    guess = [None] * n
    solution = []

    def recursion(index):
        if index == n:
            solution.append("".join(guess))
            return
        val = observed[index]
        for num in data[val]:
            guess[index] = num
            recursion(index + 1)
        return solution

    return recursion(0)


print(get_pins('369'))
