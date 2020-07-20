def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    table = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != table[-1]:
            table.append(iterable[i])
    return table


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
