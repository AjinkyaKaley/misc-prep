class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:

    def invertTree(self, root):
        
        if root is None:
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root
    
    def printBT(self, root):

        if root is None:
            return

        self.printBT(root.left)
        print(root.value)
        self.printBT(root.right)

sln = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
sln.printBT(root)
print("******** INVERTED ********")
sln.invertTree(root)
sln.printBT(root)



