class HighScoreTable:
    def __init__(self, size):
        self.size = size
        self.scores = []

    def update(self, value):
        self.scores.append(value)
        self.scores.sort(reverse=True)
        if len(self.scores) > self.size: self.scores = self.scores[:self.size]

    def reset(self):
        self.scores = []


table = HighScoreTable(3)
print(table.scores)
print(table.update(10))
print(table.update(8))
print(table.update(12))
print(table.update(5))
print(table.update(10))
print(table.scores)
table.reset()
print(table.scores)
