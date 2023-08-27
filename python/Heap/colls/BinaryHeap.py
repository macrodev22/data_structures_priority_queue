class BinaryHeap():
    elements = []
    isMaxHeap = True

    def __init__(self, minHeap=False, collection=None) -> None:
        self.isMaxHeap = not minHeap
        self.elements.append(0)
        if collection:
            for item in collection:
                self.addItem(item)

    def extractTop(self):
        top = self.elements[1]
        size = len(self.elements)
        self.elements[1] = self.elements[size - 1]
        self.elements.__delitem__(size-1)
        self.siftDown(1)
        return top

    def size(self):
        return len(self.elements)-1

    def leftChild(self, i):
        return i*2

    def rightChild(self, i):
        return (i*2)+1

    def parent(self, i):
        return i//2

    def swap(self, a, b):
        tmp = self.elements[a]
        self.elements[a] = self.elements[b]
        self.elements[b] = tmp

    def buildHeap(self):
        size = len(self.elements)
        for i in range(1, size-1):
            self.siftDown(i)

    def siftUp(self, i):
        if self.isMaxHeap:
            maxIndex = i
            parentIndex = self.parent(maxIndex)
            while (self.elements[maxIndex] > self.elements[parentIndex] and maxIndex > 1):
                self.swap(maxIndex, parentIndex)
                maxIndex = parentIndex
                parentIndex = self.parent(maxIndex)
        else:
            # Min heap
            minIndex = i
            parentIndex = self.parent(minIndex)
            while (minIndex > 1 and self.elements[minIndex] < self.elements[parentIndex]):
                self.swap(minIndex, parentIndex)
                minIndex = parentIndex
                parentIndex = self.parent(minIndex)

    def siftDown(self, i):
        size = len(self.elements)
        if self.isMaxHeap:
            maxIndex = i
            leftChild = self.leftChild(maxIndex)
            if leftChild < size and self.elements[leftChild] > self.elements[maxIndex]:
                maxIndex = leftChild
            rightChild = self.rightChild(i)
            if rightChild < size and self.elements[rightChild] > self.elements[maxIndex]:
                maxIndex = rightChild
            if (i != maxIndex):
                self.swap(maxIndex, i)
                self.siftDown(maxIndex)

        else:
            # Min heap
            minIndex = i
            leftChild = self.leftChild(i)
            rightChild = self.rightChild(i)
            if leftChild < size and self.elements[leftChild] < self.elements[minIndex]:
                minIndex = leftChild
            if rightChild < size and self.elements[rightChild] < self.elements[minIndex]:
                minIndex = rightChild
            if (minIndex != i):
                self.swap(i, minIndex)
                self.siftDown(minIndex)

    def addItem(self, item):
        self.elements.append(item)
        self.siftUp(len(self.elements) - 1)
