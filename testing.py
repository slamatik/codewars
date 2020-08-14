class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    if len(students) == 1:
        return students[0].name
    values = []
    for i in range(len(students)):
        values.append(students[i].fives * 5 + students[i].tens * 10 + students[i].twenties * 20)
    index = values.index(max(values))
    if all(x == values[0] for x in values):
        return "all"
    return students[index].name


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

print(most_money([phil, cam, geoff]))
print(most_money([cam, geoff]))
