def max_sequence(arr):
    if not arr:
        return 0
    if all(i < 0 for i in arr):
        return 0
    table = [arr[0]]
    for i in range(1, len(arr)):
        table.append(max(table[-1] + arr[i], arr[i]))
    return max(table)


print(max_sequence([]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
