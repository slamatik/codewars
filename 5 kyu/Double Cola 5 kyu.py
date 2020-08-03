data = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


def who_is_next(names, r):
    if r <= 5:
        return names[r - 1]
    start = 1
    letter_count = 1
    while start < r:
        start += len(names) * letter_count
        letter_count *= 2
    letter_count //= 2
    cnt = len(names)
    if start == r:
        return names[0]
    while True:
        start -= letter_count
        cnt -= 1
        if start == r:
            return names[cnt]
        elif start > r:
            continue
        else:
            return names[cnt]


print(who_is_next(data, 1))
print(who_is_next(data, 52))
print(who_is_next(data, 7230702951))
