from math import floor


def f(k, n):
    table = [1]
    if n == 0:
        return table[n]
    else:
        for i in range(1, n+1):
            table.append(table[i - 1] + table[floor(i / k)])
    return table[-1]


print(f(2, 3))
print(f(2, 200))
print(f(2, 1000))
print(f(7, 500))
print(f(100, 0))

