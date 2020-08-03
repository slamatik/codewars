def list_squared(m, n):
    solution = []
    for i in range(m, n + 1):
        if check_square(square_divs(i)):
            solution.append([i, square_divs(i)])
    return solution


def square_divs(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n / i == i:
            divisors.append(i)
        elif n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    divisors = [i ** 2 for i in divisors]
    return sum(divisors)


def check_square(n):
    return int(n ** 0.5) ** 2 == n


print(list_squared(1, 250))
print(list_squared(42, 250))
print(list_squared(250, 500))
