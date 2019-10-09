
import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def bfs(self,r):
        q = []
        q.append(r)
        while q:
            root = q.pop(0)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
            print(root.val)
    
sln = Solution()   
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
sln.bfs(root)