def productFib(prod):
    fib = [0, 1]
    while (fib[-1] * fib[-2]) < prod:
        fib.append(fib[-1] + fib[-2])
    return [fib[-2], fib[-1], fib[-1] * fib[-2] == prod]


print(productFib(714))
print(productFib(4895))
print(productFib(5895))
