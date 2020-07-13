from sys import maxsize as inf

# bottom up
def shortest_steps_to_num(num):
    table = [inf for i in range(num + 1)]
    table[0] = 0
    table[1] = 1
    table[2] = 1
    for column in range(3, num + 1):
        if column % 2 == 0:
            table[column] = table[column//2] + 1
        else:
            table[column] = table[column-1] + 1
    return table[-1]


print(shortest_steps_to_num(10000))

# recursive
# def shortest_steps_to_num(num):
#     memo = {1: 0}
#
#     if num in memo:
#         return memo[num]
#
#     else:
#         if num % 2 != 0:
#             temp = shortest_steps_to_num(num - 1) + 1
#             memo[num] = temp
#             return temp
#         else:
#             temp = shortest_steps_to_num(num // 2) + 1
#             memo[num] = temp
#             return temp