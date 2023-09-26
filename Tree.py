class Tree():
    """
    树的抽象基类
    """

    # 叫做位置的内嵌类，用于封装节点
    class Node():

        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

    def root(self):
        """
        return 根节点的position
        """
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """

        :param p:一个位置对象
        :return: 返回p的父节点的position对象，如果p是根节点则饭后空
        """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """

        :param p:一个位置对象
        :return: 返回该位置的孩子节点的数量
        """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """

        :param p: 一个位置对象
        :return: 返回位置p的孩子的迭代
        """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """

        :return: 返回整个树的节点个数
        """
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """
        计算节点在树中的深度
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p):
        """
        计算节点在树中的深度
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))
