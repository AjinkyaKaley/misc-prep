
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root:
            self.connect(root.left)
            self.connect(root.right)
            if root.left != None:
                root.left.next = root.right
        return root

sln = Solution()
root = Node(1,Node(2,Node(4,None,None,None),Node(5,None,None,None),None), Node(3,Node(6,None,None,None),Node(7,None,None,None),None),None)

sln.connect(root)
        