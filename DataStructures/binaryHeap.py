class Node:
    def __init__(self, rootValue):
        self.value = rootValue
        self.left = None
        self.right = None

class BinaryHeap:

    def __init__(self):
        self.heap = []

    def extractMin(self):
        item = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        del self.heap[-1]
        self.heapifyDown()
        return item

    def heapifyDown(self):
        if len(self.heap) == 1:
            return
        index = 0
        while index < len(self.heap):
            leftChildIndex = 2*index + 1
            if leftChildIndex >= len(self.heap):
                return
            childIndex = leftChildIndex          
            rightChildIndex = 2*index + 2
            if rightChildIndex < len(self.heap) and self.heap[leftChildIndex]>self.heap[rightChildIndex]:
                childIndex = rightChildIndex
            if self.heap[index] < self.heap[childIndex]:
                return
            else:
                temp = self.heap[index]
                self.heap[index] = self.heap[childIndex]
                self.heap[childIndex] = temp
                index = childIndex

    def heapifyUp(self, index):
        if len(self.heap) == 1:
            return
        parentIndex = (index-1) // 2
        while self.heap[index] < self.heap[parentIndex] and parentIndex >= 0:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index = parentIndex
            parentIndex = (index-1) // 2


    def insert(self,heap, element):
        heap.append(element)
        self.heapifyUp(len(heap)-1)

    def findEntry(self, key):

        index = 0

        while index < len(self.heap):
            if self.heap[index] == key:
                return index
            leftChildIndex = 2*index + 1
            if leftChildIndex >= len(self.heap):
                return
            index = leftChildIndex          
            rightChildIndex = 2*index + 2
            if rightChildIndex < len(self.heap) and self.heap[leftChildIndex]>self.heap[rightChildIndex]:
                index = rightChildIndex

        return -1

    def deleteEntry(self, key):
        index = self.findEntry(key)
        if index >= 0:
            self.heap[0] = self.heap[len(self.heap)-1]
            del self.heap[-1]
            self.heapifyDown()

    def constructHeapFromArray(self, elements, index, root):
        
        if index == len(elements)-1:
            return Node(elements[index])
        elif index >= len(elements) -1 :
            return None
        
        root = Node(elements[index])
        leftChildIndex = 2*index + 1
        root.left = self.constructHeapFromArray(elements,leftChildIndex, root.left)
        rightChildIndex = 2*index + 2
        root.right = self.constructHeapFromArray(elements,rightChildIndex, root.right)

        return root

sln = BinaryHeap()
# sln.constructHeapFromArray([1,3,6,5,9,8],0,sln.heap)
sln.insert(sln.heap,3)
sln.insert(sln.heap,2)
sln.insert(sln.heap,1)
sln.insert(sln.heap,15)
sln.insert(sln.heap,5)
sln.insert(sln.heap,4)
sln.insert(sln.heap,45)
print(sln.heap)
sln.extractMin()
print(sln.heap)
sln.deleteEntry(2)