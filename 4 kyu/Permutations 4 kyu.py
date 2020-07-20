def permutations(string):
    a = list(string)
    n = len(string)
    solution = []

    def permute(a, l, r):
        if l == r:
            solution.append("".join(a))
        else:
            for i in range(l, r + 1):
                a[i], a[l] = a[l], a[i]
                permute(a, l + 1, r)
                a[i], a[l] = a[l], a[i]
        return solution

    return set(permute(a, 0, n - 1))


print(permutations("a"))
print(permutations("ab"))
print(permutations("aabb"))
