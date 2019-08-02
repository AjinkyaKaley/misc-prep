class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        seen = []

        def sum_(node):
            if not node:
                return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.right.left = TreeNode(2)
root.right.right = TreeNode(20)
sln = Solution()
print(sln.checkEqualTree(root))