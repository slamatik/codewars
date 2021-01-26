def sum_of_intervals(intervals):
    return len(set([n for i in intervals for n in range(i[0], i[1])]))


print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
