class Vector:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"({','.join([str(i) for i in self.data])})"

    def add(self, vector):
        if len(self.data) != len(vector.data):
            raise ValueError
        return Vector([self.data[i] + vector.data[i] for i in range(len(self.data))])

    def subtract(self, vector):
        return Vector([self.data[i] - vector.data[i] for i in range(len(self.data))])

    def dot(self, vector):
        return sum([self.data[i] * vector.data[i] for i in range(len(self.data))])

    def norm(self):
        return sum([i ** 2 for i in self.data]) ** 0.5

    def equals(self, vector):
        return True if self.data == vector.data else False


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])

print(a.add(b).equals(Vector([4, 6, 8])))
print(a.subtract(b).equals(Vector([-2, -2, -2])))
print(a.dot(b))
print(a.norm())
