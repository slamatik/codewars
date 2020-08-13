def valid_parentheses(string):
    left_bracket_count = 0
    for i in string:
        if i == "(":
            left_bracket_count += 1
        elif i == ")":
            left_bracket_count -= 1
        if left_bracket_count < 0:
            return False
    return True if left_bracket_count == 0 else False


print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))
