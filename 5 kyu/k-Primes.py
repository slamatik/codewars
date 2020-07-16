def count_Kprimes(k, start, end):
    solution = []
    for i in range(start, end + 1):
        if factorization(i) == k:
            solution.append(i)
    return solution


def factorization(n):
    if n == 0:
        return 0
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            cnt += 1
            n //= i

    if n > 1:
        cnt += 1

    return cnt


def puzzle(s):
    one_prime = [i for i in range(2, s) if factorization(i) == 1]
    three_prime = [i for i in range(2, s) if factorization(i) == 3]
    seven_prime = [i for i in range(128, s) if factorization(i) == 7]
    total = 0
    for i in seven_prime:
        for a in three_prime:
            for b in one_prime:
                if i + a + b == s:
                    total += 1
    return total


print(count_Kprimes(2, 0, 100))
print(count_Kprimes(3, 0, 100))
print(count_Kprimes(5, 1000, 1100))
print(count_Kprimes(5, 500, 600))
print(puzzle(143))
