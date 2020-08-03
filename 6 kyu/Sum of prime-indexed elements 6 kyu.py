def total(arr):
    m = len(arr) - 1
    primes = sieve(m)
    tot = 0
    for i in primes:
        tot += arr[i]
    return tot


def sieve(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [s for s in range(2, n + 1) if primes[s]]


print(total([1, 2, 3, 4, 5, 6]))
print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
