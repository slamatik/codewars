def solve(s):
    if s == s[::-1]:
        return "OK"
    else:
        index = 0
        while index < len(s):
            temp = s[0:index] + s[index + 1:]
            if temp == temp[::-1]:
                return "remove one"
            index += 1
        return "not possible"


print(solve("abba"))
print(solve("abbaa"))
print(solve("abbaab"))
print(solve("hannah"))
