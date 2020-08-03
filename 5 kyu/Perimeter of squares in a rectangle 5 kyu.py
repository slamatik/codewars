def perimeter(n):
    fib = [1, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    return sum(fib) * 4


print(perimeter(5))
print(perimeter(7))
print(perimeter(20))
print(perimeter(30))
print(perimeter(100))
