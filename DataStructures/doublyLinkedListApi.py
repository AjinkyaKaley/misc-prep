# from .DoublyLinkedListNode import DoublyLinkedListNode


class DoublyLinkedListNode:
    def __init__(self, value):
        self.nextPtr = None
        self.backptr = None
        self.value = value

class doublyLinkedListApi:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        newNode = DoublyLinkedListNode(value)
        if self.head:
            self.tail.nextPtr = newNode
            newNode.backptr = self.tail
            self.tail = self.tail.nextPtr
        else:
            self.head = newNode
            self.tail = self.head
        
    def find(self, value):
        runnerNode = self.head
        while runnerNode:
            if runnerNode.value == value:
                return runnerNode
            runnerNode = runnerNode.nextPtr
        return None

    def delete(self, value):
        NodeToDelete = self.find(value)
        try:
            if NodeToDelete:
                if NodeToDelete.backptr and NodeToDelete.nextPtr:
                    NodeToDelete.backptr.nextPtr = NodeToDelete.nextPtr
                    NodeToDelete.nextPtr = None
                elif NodeToDelete.backptr and not NodeToDelete.nextPtr:
                    NodeToDelete.backptr.nextPtr = None
                    self.tail = self.tail.backptr
                elif not NodeToDelete.backptr and NodeToDelete.nextPtr:
                    self.head = NodeToDelete.nextPtr
            else:
                raise Exception('Value to delete does not exist in double linked list')
        except Exception as ex:
            print(ex.args)

    def createDDL(self, items):
        for i in range(len(items)):
            self.insert(items[i])
    
    def printDDL(self):
        runnerPtr = self.head
        while runnerPtr:
            print(runnerPtr.value)
            runnerPtr = runnerPtr.nextPtr

def main():
    ddl = doublyLinkedListApi()
    ddl.createDDL([1, 2, 3, 4, 5])
    ddl.insert(6)
    ddl.delete(3)
    ddl.delete(1)
    ddl.delete(5)
    ddl.printDDL()

if __name__ == '__main__':
    main()
