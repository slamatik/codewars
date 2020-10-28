from string import ascii_letters


def find_missing_letter(chars):
    let = ascii_letters
    p = 0
    while let[p] != chars[0]:
        p += 1

    for i in range(len(chars)):
        if chars[i] == let[p]:
            p += 1
        else:
            return let[p]

    # return p, let[p]

st = ["a","b","c","d","f"]
# st = ["O", "Q", "R", "S"]
print(find_missing_letter(st))
