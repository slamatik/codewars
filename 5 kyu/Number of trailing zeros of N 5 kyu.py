def zeros(n):
    total = 0
    divider = 5
    while divider < n:
        total += n // divider
        divider *= 5
    return total


print(zeros(100000))
