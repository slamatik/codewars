def create_phone_number(n):
    n = [str(i) for i in n]
    return f"({''.join(n[:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
