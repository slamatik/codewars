def find_nb(m):
    total = 0
    i = 0
    while m:
        i += 1
        total += i**3
        if total == m:
            return i
        if total > m:
            break
    return -1


print(find_nb(1071225))
print(find_nb(4183059834009))
print(find_nb(135440716410000))
print(find_nb(91716553919377))
