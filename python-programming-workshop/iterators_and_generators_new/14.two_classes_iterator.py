
from collections import deque

class Node(object):

    def __init__(self, title, children=None):
        self.title = title
        self.children = children or []

    def __str__(self):
        return self.title

    def __iter__(self):
        yield self
        for child in self.children:
            for node in child:
                yield node

class Iterator(object):

    def __init__(self, root):
        self.stack = []
        self.current = root

    def next(self):
        if self.current is None:
            return None

        self.stack.append(self.current)
        self.current.visited = True

        # Root case
        if len(self.stack) == 1:
            return self.current

        while self.stack:
            self.current = self.stack[-1]
            for child in self.current.children:
                if not child.visited:
                    self.current = child
                    return child

            self.stack.pop()


def node_depth_first_iter(node):
    stack = deque([node])
    while stack:
        # Pop out the first element in the stack
        node = stack.popleft()
        yield node
        # push children onto the front of the stack.
        # Note that with a deque.extendleft, the first on in is the last
        # one out, so we need to push them in reverse order.
        stack.extendleft(reversed(node.children))

tree = Node(
    'A', [
        Node('B', [
            Node('C', [
                Node('D')
                ]),
            Node('E'),
            ]),
        Node('F'),
        Node('G'),
        ])

iter = Iterator(tree)

out = object()
while out:
    out = iter.next()
    print(out)

expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Test recursive generator using Node.__iter__
assert [str(n) for n in tree] == expected

# test non-recursive Iterator
assert [str(n) for n in node_depth_first_iter(tree)] == expected
