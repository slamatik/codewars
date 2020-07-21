def valid_solution(board):
    for i in board:
        if len(set(i)) != len(i):
            return False
    for x in range(9):
        temp = []
        for y in range(9):
            temp.append(board[y][x])
        if len(set(temp)) != len(temp):
            return False
    for i in range(9):
        row = 3 * (i // 3)
        col = 3 * (i % 3)
        cube = []
        for j in range(9):
            y = row + j // 3
            x = col + j % 3
            cube.append(board[y][x])
        if len(set(cube)) != len(cube):
            return False
    return True


print(valid_solution(
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2], [4, 5, 6, 7, 8, 9, 1, 2, 3],
     [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7],
     [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
