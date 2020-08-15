class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = '\n'.join([''.join(['0' for x in range(width)]) for y in range(height)])

    def plot_point(self, x, y):
        grid = self.grid.split("\n")
        for i in range(len(grid)):
            grid[i] = list(grid[i])
        grid[y - 1][x - 1] = "X"
        self.grid = '\n'.join([''.join([t for t in grid[d]]) for d in range(len(grid))])

    def __repr__(self):
        pass


g = Grid(10, 10)
# print(g.grid)
g.plot_point(5, 3)
print(g.grid)
