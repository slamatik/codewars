def reverse(seq):
    left = 0
    right = len(seq) - 1
    while left < right:
        seq[left], seq[right] = seq[right], seq[left]
        left += 1
        right -= 1
    return seq


print(reversed([1, 2, 3, 4, 5, 6]))
