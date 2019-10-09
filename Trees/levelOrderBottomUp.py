# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        level=0
        result=dict()
        t = self.helper(root, level, result)
        return t.values()
    
    def helper(self,root, level, result):
        if root is None:
            return result
        
        if level in result:
            result.get(level).append(root.val)
        else:
            result[level] = [root.val]
        self.helper(root.left, level+1, result)
        self.helper(root.right, level+1, result)
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
sln = Solution()
print(sln.levelOrderBottom(root))