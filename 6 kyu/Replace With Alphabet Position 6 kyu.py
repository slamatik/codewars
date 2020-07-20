def alphabet_position(text):
    from string import ascii_lowercase
    alphabet = {x: y for y, x in enumerate(ascii_lowercase, 1)}
    solution = [str(alphabet[i]) for i in text.lower() if i in ascii_lowercase]
    return " ".join(solution)


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
