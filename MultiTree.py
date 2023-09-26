class Queue:
    def __init__(self,max_size):
        self.max_size = int(max_size)
        self.queue = []

    def put(self,data):
        if self.max_size > 0:
            if self.full():
                raise ValueError('Queue is full!')
            else:
                self._put(data)

    def get(self):
        if self._queue_size() > 0:
            result = self._get()
            empty_flag = False
        else:
            result = None
            empty_flag = True
        return result

    def empty(self):
        if self._queue_size() == 0:
            return True
        else:
            return False

    def full(self):
        if self._queue_size() == self.max_size:
            return True
        else:
            return False

    def _put(self,data):
        self.queue.append(data)

    def _get(self):
        result = self.queue[0]
        self.queue.pop(0)
        return result

    def _queue_size(self):
        return len(self.queue)

class TreeRoot:
    def __init__(self,root_node):
        self.root = root_node

    def travel_dbfs(self):#图的深度遍历
        stack_list = []
        visited = []
        stack_list.append(self.root)
        visited.append(self.root)
        while len(stack_list) > 0:
            x = stack_list[-1]
            for w in x.child_list:
                if not w in visited:
                    print(w.name)
                    visited.append(w)
                    stack_list.append(w)
                    break
            if stack_list[-1] == x:
                stack_list.pop()

    def travel_bfs(self):#图的广度遍历
        queue = Queue(100000)
        visited = []
        queue.put(self.root)
        visited.append(self.root)
        while not queue.empty():
            v =queue.get()
            i = 1
            try:
                w=v.child_list[i]
            except IndexError:
                w = None
            while w:
                if not w in visited:
                    print(w.name)
                    visited.append(w)
                    queue.put(w)
                    i = i+1
                    try:
                        w = v.child_list[i]
                    except IndexError:
                        w = None
        return visited

    def search(self,keyword):
        visited_list = self.travel_bfs()
        for v in visited_list:
            if v.data == keyword:
                return v
        return None

    def built(self,node):
        parent = node.parent
        v = self.search(parent.data)
        v.child_list.append(node)


class TreeNode:
    def __init__(self,name,groupid):
        self.parent = None
        self.child_list = []
        self.name = name
        self.groupid = groupid