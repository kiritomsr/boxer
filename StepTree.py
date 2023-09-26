from map import BoxMap
import numpy as np
import copy


class Node:
    # image = []
    solution = []

    def __init__(self, p, boxmap, action):
        self.boxmap = boxmap
        self.parent = p
        self.action = action
        self.history = []
        self.childs = []
        self.leaf = 0

        if self.parent is None:
            self.root = True
            self.history.append(self.boxmap.grids)
            self.pas = []
            self.height = 0
        else:
            self.root = False
            self.generate_steps()
            self.height = self.parent.height + 1

    def add_child(self, boxmap, pa):
        self.childs.append(Node(self, boxmap, pa))

    def next_map(self, pa):
        pos, move = pa
        now_grids = copy.copy(self.boxmap.grids)

        now_grids[self.boxmap.pos[0]][self.boxmap.pos[1]] = 0
        now_grids[pos[0] + move[0]][pos[1] + move[1]] = 3
        now_grids[pos[0] + 2 * move[0]][pos[1] + 2 * move[1]] = 2
        # print(now_grids)
        return BoxMap(now_grids, self.boxmap.targets)

    def generate_child(self):
        if not self.boxmap.pa:
            self.leaf = 1
        for pa in self.boxmap.pa:
            # print(pa)
            self.add_child(self.next_map(pa), pa)

    def generate_steps(self):
        self.history = copy.copy(self.parent.history)
        self.pas = copy.copy(self.parent.pas)
        self.kill_node()
        if self.leaf == 2:
            self.history.append(self.boxmap.grids)
            self.pas.append(self.action)
            # Node.image.append(self.boxmap.grids)

        if self.leaf == 0:
            self.history.append(self.boxmap.grids)
            self.pas.append(self.action)
            # Node.image.append(self.boxmap.grids)
            # self.generate_child()

    def is_same_grids(self, comp_grids):
        it = np.nditer(comp_grids, flags=['multi_index'])
        while not it.finished:
            if comp_grids[it.multi_index[0]][it.multi_index[1]] != self.boxmap.grids[it.multi_index[0]][
                it.multi_index[1]]:
                return False
            it.iternext()
        return True

    def kill_node(self):
        if self.boxmap.end:
            self.leaf = 2
            # print('end')
            return
        # for grids in Node.image:
        #     if self.is_same_grids(grids):
        #         self.leaf = 1
        #         # print('kill')
        #         return
        for grids in self.history:
            if self.is_same_grids(grids):
                self.leaf = 1
                # print('kill')
                return
        # print('continue')


def iter(node):
    node.generate_child()
    # print('height: ' + str(node.height)+ '   pas: ' +str(node.pas)+ '   leaf: ' +str(node.leaf))
    for child in node.childs:
        print('height: ' + str(child.height) + '   pas: ' + str(child.pas) + '   leaf: ' + str(child.leaf))
        if child.leaf == 0:
            iter(child)

        if child.leaf == 1:
            return

        if child.leaf == 2:
            Node.solution = child.history
            return child.history


def logic_use(node):
    # waiting for check
    stack_list = []
    # checked node

    stack_list.append(node)

    # while true
    while len(stack_list) > 0:
        # select one node from stack
        point = stack_list[-1]
        print('stack: ' + str(len(stack_list)) + '   height: ' + str(point.height) + '   pas: ' + str(point.pas) + '   leaf: ' + str(point.leaf))
        # finish
        if point.leaf == 2:
            return point.history

        # mark this node as checked
        stack_list.pop()

        # if node can bred
        if point.leaf != 1:
            point.generate_child()
            for child in point.childs:

                stack_list.append(child)


def choose_chapter(num):
    if num == 70:
        input_map = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 1, 1],
            [1, 0, 0, 2, 2, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        bm = BoxMap(input_map, [(4, 2), (4, 4)])

    if num == 111:
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

    if num == 95:
        input_map = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1],
            [1, 0, 2, 0, 2, 0, 1],
            [1, 0, 0, 1, 2, 3, 1],
            [1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]

        bm = BoxMap(input_map, [(5, 1), (5, 2), (5, 3)])

    if num == 98:
        input_map = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 0, 1],
            [1, 1, 0, 2, 2, 3, 1],
            [1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]

        bm = BoxMap(input_map, [(2, 2), (1, 3), (2, 3)])

    return bm


def main():

    bm = choose_chapter(98)

    start = Node(None, bm, None)
    print(logic_use(start))

    # start.generate_child()
    # for child in start.childs:
    #     print('height: ' + str(child.height)+ '   pas: ' +str(child.pas))
    #     child.generate_child()
    #     for grandchild in child.childs:
    #         print('height: ' + str(grandchild.height) + '   pas: ' + str(grandchild.pas))
    #         grandchild.generate_child()
    #         for ggrandchild in grandchild.childs:
    #             print('height: ' + str(ggrandchild.height) + '   pas: ' + str(ggrandchild.pas))

    # print(iter(start))
    # print(Node.solution)


if __name__ == '__main__':
    main()
