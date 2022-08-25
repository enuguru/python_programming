
class Queue:
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def enqueue(self,item):
        self._storage.append(item)

    def dequeue(self):
        try:
            item = self._storage.pop(0)
        except IndexError:
            item = None
        return item
