def decomp(n):
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

    return len(solution)


def consec_kprimes(k, arr):
    cnt = 0
    for i in range(1, len(arr)):
        if decomp(arr[i-1]) == k and decomp(arr[i]) == k:
            cnt += 1
    return cnt



data = [10005, 10030, 10026, 10008, 10016, 10028, 10004]
k = 4

print(consec_kprimes(k, data))
