from string import ascii_lowercase, ascii_uppercase


def rot13(message):
    initial = ascii_lowercase + ascii_uppercase
    rot = ascii_lowercase[13:] + ascii_lowercase[:13] + ascii_uppercase[13:] + ascii_uppercase[:13]
    translation = message.maketrans(initial, rot)
    return message.translate(translation)


print(rot13("test"))
print(rot13("Test"))
