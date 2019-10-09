from DataStructures.DoublyLinkedListNode import DoublyLinkedListNode

class LRUCache:
    def __init__(self, size):
        self.head = None    # store LRU
        self.tail = None
        self.cache = {}
        self.cacheSize = size

    def updateMRUNode(self, MRUNode):
        if MRUNode.backptr and not MRUNode.nextPtr or (not MRUNode.backptr and not MRUNode.nextPtr):
            return
        if MRUNode.backptr and MRUNode.nextPtr:
            MRUNode.backptr.nextPtr = MRUNode.nextPtr
            MRUNode.nextPtr.backptr = MRUNode.backptr
            self.tail.nextPtr = MRUNode
            MRUNode.backptr = self.tail
            self.tail = self.tail.nextPtr
            self.tail.nextPtr = None
        elif not MRUNode.backptr and MRUNode.nextPtr:
            self.head = self.head.nextPtr
            self.head.backptr = None
            self.tail.nextPtr = MRUNode
            MRUNode.backptr = self.tail
            MRUNode.nextPtr = None
            self.tail = self.tail.nextPtr

    def put(self, key, value):
        newEntry = DoublyLinkedListNode(key, value)
        if key in self.cache:
            self.cache[key].value = value
            self.updateMRUNode(self.cache[key])
        else:
            if len(self.cache) == self.cacheSize:
                LRUItem = self.head
                del self.cache[LRUItem.key]
                if len(self.cache) != 0:
                    self.head = self.head.nextPtr
                    self.head.backptr = None
                    LRUItem.nextPtr = None
            self.cache[key] = newEntry
            if not self.head:
                self.head = newEntry
                self.tail = newEntry
            else:
                self.tail.nextPtr = newEntry
                newEntry.backptr = self.tail
                self.tail = self.tail.nextPtr
    
    def get(self, key):
    
        if not key in self.cache:
            return -1

        returnItem = self.cache[key]
        self.updateMRUNode(returnItem)
        return returnItem.value

def main():
    # lru = LRUCache(4)
    # lru.put(1, 1)
    # lru.put(2, 2)
    # lru.put(3, 3)
    # lru.put(4, 4)
    # lru.get(2)
    # lru.get(2)
    # lru.get(1)
    # lru.get(3)
    # lru.get(4)

    lru = LRUCache(1)
    lru.put(2, 1)
    print(lru.get(2))
    lru.put(3, 2)
    lru.get(2)
    lru.get(3)

    # operations = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put",
    #               "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    # values = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15],
    # [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
    # lru = LRUCache(values[0][0])
    # for i in range(1, len(operations)):
    #     if operations[i] == 'put':
    #         lru.put(values[i][0], values[i][1])
    #     elif operations[i] == 'get':
    #         lru.get(values[i][0])

if __name__ == '__main__':
    main()
