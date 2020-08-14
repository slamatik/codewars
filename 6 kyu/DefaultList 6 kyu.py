class DefaultList:
    def __init__(self, array, default):
        self.array = array
        self.default = default

    def check(self, value):
        if value < -len(self.array) or value >= len(self.array):
            return False
        else:
            return True

    def extend(self, values):
        self.array += values

    def append(self, value):
        self.array.append(value)

    def insert(self, index, value):
        self.array.insert(index, value)

    def remove(self, value):
        if value in self.array:
            self.array.remove(value)

    def pop(self, index):
        if not self.check(index):
            return self.default
        else:
            del self.array[index]

    def __getitem__(self, index):
        if not self.array:
            return self.default
        return self.array[index] if self.check(index) else self.default


lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')
print(lst[1])
print(lst[333000])
print(lst[23])
lst.extend([3, 23, 'hello', 'lists', 'word', 344])
print(lst[9])
print(lst[11])
print(lst[12])
lst.append(233344455)
lst.remove(2)
lst.remove(1)
lst.remove(3)
lst.insert(-3, 34.34)
print(lst[8])
print(lst[10])
