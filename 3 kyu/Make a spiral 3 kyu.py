def spiralize(size):
    table = [[0 for i in range(size)] for y in range(size)]

    row = 0
    col = size - 1

    for i in range(size):
        table[0][i] = 1

    size -= 1
    cnt = size

    while cnt:
        for i in range(size):
            row += 1
            table[row][col] = 1
        cnt -= 1
        if cnt == 0: break

        for i in range(size):
            col -= 1
            table[row][col] = 1
        cnt -= 1
        size -= 2
        if cnt == 0: break

        for i in range(size):
            row -= 1
            table[row][col] = 1
        cnt -= 1
        if cnt == 0: break

        for i in range(size):
            col += 1
            table[row][col] = 1
        cnt -= 1
        size -= 2
        if cnt == 0: break
    return table