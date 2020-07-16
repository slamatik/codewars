def find_emirp(n):
    primes = sieve(n)
    data = []
    if n < 13:
        return [0,0,0]
    for i in primes:
        temp = int(str(i)[::-1])
        if prime_check(temp) and str(i) != str(temp):
            data.append(i)
    return [len(data), max(data), sum(data)]


def sieve(n):
    solution = []
    primes = [True for i in range(n + 1)]
    p = 2
    while p * 2 <= n:
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    for i in range(2, n + 1):
        if primes[i]:
            solution.append(i)
    return solution


def prime_check(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


print(find_emirp(10))
print(find_emirp(50))
print(find_emirp(903886))
