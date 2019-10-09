class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def upsideDownBinaryTree(self, root):

        if not root or not root.left:
            return root
        lRoot = self.upsideDownBinaryTree(root.left)
        rMost = lRoot
        while rMost.right:
            rMost = rMost.right
        rMost.right = TreeNode(root.val)
        rMost.left = root.right
        root = lRoot
        return root

        # if not root or not root.left:
        #     return root
        # lRoot = self.upsideDownBinaryTree(root.left)
        # rMost = lRoot
        # while rMost.right:
        #     rMost = rMost.right
        # root, rMost.left, rMost.right = lRoot, root.right, TreeNode(root.val)
        # return root

    def upsideDownBinaryTreeAlternate(self, root):
        if not root:
            return root

        if not root.left and not root.right:
            return root

        flippedRoot = self.upsideDownBinaryTreeAlternate(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return flippedRoot


sln = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sln.upsideDownBinaryTree(root)
