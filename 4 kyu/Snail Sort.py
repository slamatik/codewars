def snail(snail_map):
    row_start = 0
    row_end = len(snail_map) - 1
    col_start = 0
    col_end = len(snail_map) - 1
    solution = []

    if len(snail_map[0]) == 0:
        return solution

    while row_start <= row_end and col_start <= col_end:
        # Top Row
        for col in range(col_start, col_end + 1):
            solution.append(snail_map[row_start][col])
        row_start += 1

        # Right Col
        for row in range(row_start, row_end + 1):
            solution.append(snail_map[row][col_end])
        col_end -= 1

        # Bottom Row
        for col in range(col_end, col_start - 1, -1):
            solution.append(snail_map[row_end][col])
        row_end -= 1

        # Left Col
        for row in range(row_end, row_start - 1, -1):
            solution.append(snail_map[row][col_start])
        col_start += 1
    return solution


# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# array = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12],
#          [13, 14, 15, 16]]

array = [[]]

print(snail(array))
