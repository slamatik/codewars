def sum_for_list(lst):
    factors = get_prime_factors(lst[0])
    for i in range(1, len(lst)):
        factors += get_prime_factors(lst[i])
    factors = set(factors)
    solution = []
    for fac in factors:
        num_sum = 0
        for num in lst:
            if num % fac == 0:
                num_sum += num
        solution.append([fac, num_sum])
    return sorted(solution)


def get_prime_factors(n):
    if n < 0:
        n = -n
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            primes.append(i)
            n //= i
    if n > 1:
        primes.append(n)
    return list(set(primes))


print(sum_for_list([12, 15]))
print(sum_for_list([15, 30, -45]))
print(sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]))
