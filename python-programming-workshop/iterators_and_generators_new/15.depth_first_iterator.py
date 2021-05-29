
class Node(object):
    def __init__(self, value):
        self._value = value
        self._childeren = []

    def add_child(self, node):
        self._childeren.append(node)

    def __repr__(self):
        return "Node{!r}".format(self._value)

    def __iter__(self):
        return iter(self._childeren)

    def depth_first(self):
        yield self # first return current node
        for child in self:
            yield from child.depth_first()

    def breadth_first(self):
        stack = [self]
        while stack:
            print(">>> stack: " , stack)
            cur_node, stack = stack[0], stack[1:]
            yield cur_node
            for child in cur_node:
                stack.append(child)

root = Node(0)

child1 = Node(1)
child2 = Node(2)

child3 = Node(3)
child4 = Node(4)
root.add_child(child1)
root.add_child(child2)

child1.add_child(child3)
child1.add_child(child4)
child2.add_child(Node(5))
child2.add_child(Node(6))
child3.add_child(Node(7))
child4.add_child(Node(8))


for ch in root.breadth_first():
    print(ch)

for ch in root.depth_first():
    print(ch)
