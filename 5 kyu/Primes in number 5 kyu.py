def primeFactors(n):
    solution = []
    while n % 2 == 0:
        solution.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            solution.append(i)
            n //= i
    if n > 1:
        solution.append(n)
    return print_result(solution)


def print_result(nums):
    solution = ""
    uniques = sorted(set(nums))
    for i in uniques:
        temp = nums.count(i)
        if temp == 1:
            solution += f"({i})"
        else:
            solution += f"({i}**{temp})"
    return solution


print(primeFactors(7775460))
