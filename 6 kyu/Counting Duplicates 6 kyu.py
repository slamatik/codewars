def duplicate_count(text):
    data = set(text.lower())
    cnt = 0
    for i in data:
        if text.lower().count(i) > 1:
            cnt += 1
    return cnt


print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))
