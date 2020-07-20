def zero(n=None):
    if n is None:
        return 0
    else:
        if n[0] == "+":
            return 0 + n[1]
        if n[0] == "-":
            return 0 - n[1]
        if n[0] == "//":
            return 0 // n[1]
        if n[0] == "*":
            return 0 * n[1]


def one(n=None):
    if n is None:
        return 1
    else:
        if n[0] == "+":
            return 1 + n[1]
        if n[0] == "-":
            return 1 - n[1]
        if n[0] == "//":
            return 1 // n[1]
        if n[0] == "*":
            return 1 * n[1]


def two(n=None):
    if n is None:
        return 2
    else:
        if n[0] == "+":
            return 2 + n[1]
        if n[0] == "-":
            return 2 - n[1]
        if n[0] == "//":
            return 2 // n[1]
        if n[0] == "*":
            return 2 * n[1]


def three(n=None):
    if n is None:
        return 3
    else:
        if n[0] == "+":
            return 3 + n[1]
        if n[0] == "-":
            return 3 - n[1]
        if n[0] == "//":
            return 3 // n[1]
        if n[0] == "*":
            return 3 * n[1]


def four(n=None):
    if n is None:
        return 4
    else:
        if n[0] == "+":
            return 4 + n[1]
        if n[0] == "-":
            return 4 - n[1]
        if n[0] == "//":
            return 4 // n[1]
        if n[0] == "*":
            return 4 * n[1]


def five(n=None):
    if n is None:
        return 5
    else:
        if n[0] == "+":
            return 5 + n[1]
        if n[0] == "-":
            return 5 - n[1]
        if n[0] == "//":
            return 5 // n[1]
        if n[0] == "*":
            return 5 * n[1]


def six(n=None):
    if n is None:
        return 6
    else:
        if n[0] == "+":
            return 6 + n[1]
        if n[0] == "-":
            return 6 - n[1]
        if n[0] == "//":
            return 6 // n[1]
        if n[0] == "*":
            return 6 * n[1]


def seven(n=None):
    if n is None:
        return 7
    else:
        if n[0] == "+":
            return 7 + n[1]
        if n[0] == "-":
            return 7 - n[1]
        if n[0] == "//":
            return 7 // n[1]
        if n[0] == "*":
            return 7 * n[1]


def eight(n=None):
    if n is None:
        return 8
    else:
        if n[0] == "+":
            return 8 + n[1]
        if n[0] == "-":
            return 8 - n[1]
        if n[0] == "//":
            return 8 // n[1]
        if n[0] == "*":
            return 8 * n[1]


def nine(n=None):
    if n is None:
        return 9
    else:
        if n[0] == "+":
            return 9 + n[1]
        if n[0] == "-":
            return 9 - n[1]
        if n[0] == "//":
            return 9 // n[1]
        if n[0] == "*":
            return 9 * n[1]


def plus(n):
    return "+", n


def minus(n):
    return "-", n


def times(n):
    return "*", n


def divided_by(n):
    return "//", n


print(four(times(two())))
