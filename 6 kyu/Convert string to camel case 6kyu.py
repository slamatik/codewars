from string import punctuation


def to_camel_case(text):
    for c in punctuation:
        text = text.replace(c, " ")
    text = text.split()
    for i in range(1, len(text)):
        text[i] = text[i].capitalize()
    return "".join(text)


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
