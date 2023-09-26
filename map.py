import numpy as np


class BoxMap:

    def __init__(self, input, targets):
        self.grids = np.array(input)
        self.height = self.grids.shape[0]
        self.width = self.grids.shape[1]
        self.targets = targets
        if self.is_end():
            return
        self.pos = self.get_pos()
        self.feasible_region()
        self.possible_act()

    def get_pos(self):
        it = np.nditer(self.grids, flags=['multi_index'])
        while not it.finished:
            if it[0] == 3:
                return it.multi_index
            it.iternext()

    def is_empty(self, row, col):
        if self.grids[row][col] == 0 or self.grids[row][col] == 3:
            return True
        else:
            return False

    def feasible_region(self):
        self.fr = [self.pos]
        row, col = self.pos
        self.add_feasible(row, col)

    def add_feasible(self, row, col):
        neighbors = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
        for neighbor in neighbors:
            if self.is_empty(neighbor[0], neighbor[1]) and (neighbor[0], neighbor[1]) not in self.fr:
                self.fr.append((neighbor[0], neighbor[1]))
                self.add_feasible(neighbor[0], neighbor[1])

    def get_box(self):
        self.boxs = []
        it = np.nditer(self.grids, flags=['multi_index'])
        while not it.finished:
            if it[0] == 2:
                self.boxs.append(it.multi_index)
            it.iternext()

    def is_possible(self, row, col, move):
        box_now = (row + move[0], col + move[1])
        box_next = (row + 2 * move[0], col + 2 * move[1])
        if self.grids[box_now[0]][box_now[1]] == 2 and self.grids[box_next[0]][box_next[1]] == 0:
            return True
        else:
            return False

    def possible_act(self):
        self.pa = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for grid in self.fr:
            for move in moves:
                if self.is_possible(grid[0], grid[1], move):
                    self.pa.append((grid, move))

    def is_end(self):
        # print(self.grids)
        for target in self.targets:
            if self.grids[target[0]][target[1]] != 2:
                self.end = False
                return
        self.end = True


if __name__ == '__main__':
    input_map = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 2, 0, 0, 1],
        [1, 0, 3, 2, 0, 0, 1],
        [1, 0, 0, 2, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    bm = BoxMap(input_map, [(1, 1), (2, 1), (3, 1)])
    print(bm.pa)
