# Definition for a Node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        queue = [root]
        while queue:
            new_q = []
            temp = None
            while queue:
                node = queue.pop(0)
                if temp:
                    temp.next = node
                if node.left:
                    new_q += [node.left]
                if node.right:
                    new_q += [node.right]
                temp = node
            queue = new_q
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
sln = Solution()
sln.connect(root)
