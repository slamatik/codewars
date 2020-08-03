def array_diff(a, b):
    for el in b:
        while el in a:
            a.remove(el)
    return a


print(array_diff([1, 2, 2], [2]))
