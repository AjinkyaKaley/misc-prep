class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or (root.val == p.val) or (root.val == q.val):
            return root

        foundInLeftSubtree = self.lowestCommonAncestor(root.left, p, q)
        foundInRightSubtree = self.lowestCommonAncestor(root.right, p, q)

        if foundInLeftSubtree and foundInRightSubtree:
            return root
        return foundInLeftSubtree or foundInRightSubtree

root = TreeNode(3)
node1 = TreeNode(5)
root.left = node1
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
node2=TreeNode(4)
root.left.right.right = node2
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
sln = Solution()
sln.lowestCommonAncestor(root, node1, node2)




