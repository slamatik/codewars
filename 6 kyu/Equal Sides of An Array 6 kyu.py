def find_even_index(arr):
    for i in range(len(arr)):
        if i == 0:
            left = 0
            right = sum(arr[i + 1:])
        else:
            left = sum(arr[:i])
            right = sum(arr[i + 1:])
        if left == right:
            return i
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([1, 100, 50, -51, 1, 1]))
print(find_even_index([1, 2, 3, 4, 5, 6]))
print(find_even_index([20, 10, 30, 10, 10, 15, 35]))
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))
