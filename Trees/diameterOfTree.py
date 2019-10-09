from DataStructures.TreeNode import TreeNode

class Solution:
    
    def heightOfTree(self,root):
        if root == None:
            return 0
        left = self.heightOfTree(root.left)
        right = self.heightOfTree(root.right)

        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root) -> int:
        if root == None:
            return 0
        
        leftHeight = self.heightOfTree(root.left)
        rightHeight = self.heightOfTree(root.right)
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)
        
        return max(leftHeight+rightHeight+1, max(leftDiameter,rightDiameter))
        
    def diameterOfBinaryTreeOptimal(self, root):
        self.result = float("-inf")
        def helper(root):
            if root == None:
                return 0
            
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            self.result = max(self.result, leftHeight + rightHeight + 1)
            return 1 + max(leftHeight,rightHeight)

        helper(root)
        return self.result
def main():
    sln = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(8)
    root.right.right.right = TreeNode(9)
    root.right.right.right.left = TreeNode(10)
    root.right.right.right.right = TreeNode(11)
    root.right.right.right.left.right = TreeNode(12)

    print(sln.diameterOfBinaryTreeOptimal(root))

if __name__ == '__main__':
    main()
# if __name__ = '__main__':
#     main()
