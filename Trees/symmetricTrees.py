# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):

        if left is None and right is None:
            return True
        
        if (left == None and right != None) or (right == None and left != None):
            return False
        
        return self.helper(left.left, right.right) and self.helper(left.right,right.left) and left.val == right.val