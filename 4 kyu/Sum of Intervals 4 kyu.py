def sum_of_intervals(intervals):
    nums = []
    for i in intervals:
        nums += [i for i in range(i[0], i[1])]
    return len(set(nums))


print(sum_of_intervals([
    [1, 2],
    [6, 10],
    [11, 15]
]))
print(sum_of_intervals([
    [1, 4],
    [7, 10],
    [3, 5]
]))
print(sum_of_intervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
]))
