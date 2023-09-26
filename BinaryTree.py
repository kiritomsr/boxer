from Tree import Tree


class BinaryTree(Tree):
    class Node():

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(Tree.Position):

        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return isinstance(other, type(self)) and other.node is self.node

    def validate(self, p):
        """
        进行位置验证
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.parent is p.node:
            raise ValueError('p is no longer valid')
        return p.node

    def make_position(self, node):
        """
        封装节点
        """
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self.size = 0

    def __len__(self):
        return self.size

    def root(self):
        return self.make_position(self._root)

    def parent(self, p):
        node = self.validate(p)
        return self.make_position(node.parent)

    def left(self, p):
        node = self.validate(p)
        return self.make_position(node.left)

    def right(self, p):
        node = self.validate(p)
        return self.make_position(node.right)

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def num_children(self, p):
        node = self.validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self.size += 1
        self._root = self.Node(e)
        return self.make_position(self._root)

    def add_left(self, e, p):
        node = self.validate(p)
        if node.left is not None:
            raise ValueError('Left child exists')
        self.size += 1
        node.left = self.Node(e, node)
        return self.make_position(node.left)

    def add_right(self, e, p):
        node = self.validate(p)
        if node.right is not None:
            raise ValueError('Left child exists')
        self.size += 1
        node.right = self.Node(e, node)
        return self.make_position(node.right)

    def replace(self, p, e):
        node = self.validate(p)
        old = node.element
        node.element = e
        return old

    def delete(self, p):
        """
        删除该位置的节点，如果该节点有两个孩子，则会产生异常，如果只有一个孩子，
        则使其孩子代替该节点与其双亲节点连接
        """
        node = self.validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self._root:
            self._root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node
        return node.element
