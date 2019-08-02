from DataStructures.TreeNode import TreeNode

class Solution:
    def findLeaves(self, root):
        result = []
        while root:
            iterationResult = []
            root = self.helper(root, iterationResult)
            result.append(iterationResult)
            
        return result
    
    def helper(self,root, result):
        if root:
            if root.left == None and root.right == None:
                result.append(root.value)
                return None
            
            root.left = self.helper(root.left,result)
            root.right = self.helper(root.right,result)  
        return root

def main():
    sln = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(sln.findLeaves(root))

if __name__ == '__main__':
    main()

    #Example: {1, 34, 3, 98, 9, 76, 45, 4} => 998764543431