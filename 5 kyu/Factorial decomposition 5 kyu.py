def decomp(n):
    nums = [i for i in range(n, 1, -1)]
    all_factors = []
    for number in nums:
        while number % 2 == 0:
            all_factors.append(2)
            number //= 2

        for i in range(3, int(number ** 0.5) + 1, 2):
            while number % i == 0:
                all_factors.append(i)
                number //= i

        if number > 1:
            all_factors.append(number)

    solution = []
    unique_nums = sorted(set(all_factors))
    for a in unique_nums:
        temp = all_factors.count(a)
        if temp == 1:
            solution.append(f"{a}")
        else:
            solution.append(f"{a}^{temp}")

    return " * ".join(solution)


print(decomp(3988))
