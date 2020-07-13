def count_change(money, coins):
    n = len(coins)
    table = [[0 for x in range(money + 1)] for y in range(n)]

    for i in range(n):
        table[i][0] = 1

    for row in range(n):
        for column in range(1, money + 1):
            if column >= coins[row]:
                x = table[row][column-coins[row]]
            else:
                x = 0

            if row >= 1:
                y = table[row-1][column]
            else:
                y = 0

            table[row][column] = x + y

    return table[-1][-1]
