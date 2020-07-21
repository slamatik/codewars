def next_bigger(n):
    if descending(n) or len(set(str(n))) == 1:
        return -1

    number_for_permutation, remainder = extract_range(n)
    number_for_permutation_length = len(number_for_permutation) - 1
    number_for_permutation_list = list(number_for_permutation)
    solution = []

    def permute(a, l, r):
        if l == r:
            if int("".join(a)) not in solution:
                solution.append(int("".join(a)))
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                permute(a, l + 1, r)
                a[l], a[i] = a[i], a[l]
        return solution

    data = sorted(permute(number_for_permutation_list, 0, number_for_permutation_length))
    index = data.index(int(number_for_permutation))
    return int(remainder + (str(data[index + 1])))


def descending(n):
    n = [int(i) for i in str(n)]
    for i in range(1, len(n)):
        if n[i] > n[i - 1]:
            return False
    return True


def extract_range(n):
    n = str(n)
    m = len(str(n))
    solution = ""
    for i in range(m - 1, 0, -1):
        if n[i] > n[i - 1]:
            solution += n[i - 1:]
            break
    return solution, n[:i - 1]


print(next_bigger(99999))
print(next_bigger(59884848459853))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(144))
