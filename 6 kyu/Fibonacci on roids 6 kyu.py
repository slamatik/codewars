# https://www.codewars.com/kata/596144f0ada6db581200004f

def custom_fib(signature, indexes, n):
    m = len(signature)
    for i in range(m, n + 1):
        temp = 0
        for ind in indexes:
            temp += signature[-m:][ind]
        signature.append(temp)
    return signature[n]


# print(custom_fib([1, 1], [0, 1], 2))
# print(custom_fib([1, 1], [0, 1], 3))
# print(custom_fib([1, 1], [0, 1], 4))
# print(custom_fib([3, 5, 2], [0, 1, 2], 4))
# print(custom_fib([7, 3, 4, 1], [1, 1], 6))
