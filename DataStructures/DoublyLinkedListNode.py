class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.nextPtr = None
        self.backptr = None
        self.key = key
        self.value = value