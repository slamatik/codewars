from string import ascii_uppercase


class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.shift_data = ascii_uppercase[self.shift:] + ascii_uppercase[:self.shift]

    def encode(self, st):
        st = st.upper()
        data = str.maketrans(ascii_uppercase, self.shift_data)
        return st.translate(data)

    def decode(self, st):
        st = st.upper()
        data = str.maketrans(self.shift_data, ascii_uppercase)
        return st.translate(data)


c = CaesarCipher(5)
print(c.encode("Codewars"))
print(c.decode("HTIJBFWX"))
