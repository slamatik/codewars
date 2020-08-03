def find_outlier(integers):
    odd_cnt = 0
    even_cnt = 0
    for i in integers:
        if i % 2 == 0:
            even_cnt += 1
            even_num = i
        else:
            odd_cnt += 1
            odd_num = i
        if even_cnt > 1 and odd_cnt == 1:
            return odd_num
        elif even_cnt == 1 and odd_cnt > 1:
            return even_num


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
