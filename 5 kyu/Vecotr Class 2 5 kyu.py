class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
            self.magnitude = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
            self.magnitude = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def cross(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector(cx, cy, cz)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def to_tuple(self):
        return self.x, self.y, self.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return all((self.x == other.x, self.y == other.y, self.z == other.z))

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"


examples = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
v = Vector(examples[0])
# v2 = Vector(*examples[0])
v2 = Vector(examples[0])

print(v == v2)
