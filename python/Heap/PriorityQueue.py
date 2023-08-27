from Heap.colls.BinaryHeap import BinaryHeap


class PriorityQueue():
    data = None

    def __init__(self, min=False) -> None:
        self.data = BinaryHeap(minHeap=min)

    def add(self, item):
        self.data.addItem(item)

    def pop(self):
        return self.data.extractTop()

    def size(self):
        return self.data.size()
