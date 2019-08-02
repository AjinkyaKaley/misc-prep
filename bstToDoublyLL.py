
#Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.prev = None
        self.head = None
        self.helper(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
        
    def helper(self, root):
        if root is None:
            return None
        
        self.helper(root.left)
        if self.prev is None:
            self.prev = root
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
            self.prev = root
        
        self.helper(root.right)

    

sln = Solution()
root = Node(4, Node(2,Node(1, None, None),Node(3,None,None)), Node(5,None,None))
sln.treeToDoublyList(root)
