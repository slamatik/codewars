def lcs(x, y):
    n, m = len(x), len(y)

    table = [[0 for i in range(n + 1)] for i in range(m + 1)]

    for t1 in range(1, m + 1):
        for t2 in range(1, n + 1):
            if x[t2 - 1] == y[t1 - 1]:
                table[t1][t2] = 1 + table[t1 - 1][t2 - 1]
            else:
                table[t1][t2] = max(table[t1 - 1][t2], table[t1][t2 - 1])

    string = ""
    s1 = n
    s2 = m
    while s1 > 0 and s2 > 0:
        if x[s1 - 1] == y[s2 - 1]:
            string += x[s1 - 1]
            s1 -= 1
            s2 -= 1
        elif table[s2 - 1][s1] > table[s2][s1 - 1]:
            s2 -= 1
        else:
            s1 -= 1
    return string[::-1]


print(lcs("anothertest", "notatest"))
