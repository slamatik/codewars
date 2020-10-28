def sort_array(source_array):
    n = len(source_array)
    table = [0] * n
    odds = []
    zero = [False] * n
    for i in range(n):
        if source_array[i] == 0:
            zero[i] = True
        if source_array[i] % 2 == 0:
            table[i] = source_array[i]
        else:
            odds.append(source_array[i])
    odds = sorted(odds)
    for i in range(n):
        if table[i] == 0 and not zero[i]:
            table[i] = odds.pop(0)
    return table


# arr = [5, 3, 2, 8, 1, 4]
arr = [5, 3, 1, 8, 0]
print(sort_array(arr))
