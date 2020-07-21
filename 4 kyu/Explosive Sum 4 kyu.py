def exp_sum(n):
    nums = [i for i in range(n + 1)]

    table = [[0 for i in range(n + 1)] for i in range(len(nums))]

    for row in range(1, len(nums)):
        for col in range(1, len(nums)):
            if col - nums[row] == 0:
                table[row][col] = table[row - 1][col] + 1
            else:
                table[row][col] = table[row - 1][col] + table[row][col - nums[row]]
    return table[-1][-1]


print(exp_sum(100))
