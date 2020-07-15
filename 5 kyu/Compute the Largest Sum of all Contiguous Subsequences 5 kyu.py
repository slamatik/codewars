def largest_sum(arr):
    if len(arr) == 0:
        return 0
    cache = [arr[0]]
    for i in range(1, len(arr)):
        cache.append(max(arr[i], cache[-1] + arr[i]))
    return 0 if max(cache) < 0 else max(cache)


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(largest_sum(data))