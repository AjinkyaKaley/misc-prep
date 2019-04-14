# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            return True
        if (p != None and q is None) or (p is None and q != None):
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        if left is False or right is False:
            return False
        if p.val != q.val:
            return False
        else:
            return True