def longest_repetition(chars):
    if chars == "":
        return "", 0
    table = [1]
    for i in range(1, len(chars)):
        if chars[i - 1] == chars[i]:
            table.append(table[-1] + 1)
        else:
            table.append(1)
    value = max(table)
    index = table.index(value)
    return chars[index], value


print(longest_repetition("aaaabb"))
print(longest_repetition("bbbaaabaaaa"))
print(longest_repetition("cbdeuuu900"))
print(longest_repetition("abbbbb"))
print(longest_repetition("aabb"))
print(longest_repetition(""))
