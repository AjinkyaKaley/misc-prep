# from leetcode.DataStructures.TreeNode import TreeNode
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)
        self.stack = []

    def insert(self, value, root):
        
        if value <= root.value:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self.insert(value, root.left)
        elif value > root.value:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self.insert(value, root.right)

    # CLeaner insert

    def insertExpensive(self,value, root):

        if root is None:
            return TreeNode(value)
        if value <= root.value:
            root.left = self.insertExpensive(value, root.left)
        elif value > root.value:
            root.right = self.insertExpensive(value, root.right)

        return root

    def getInorderSuccessor(self, root):
        if root.left is None and root.right is None:
            return root
        return self.getInorderSuccessor(root.left)

    def deleteTreeNode(self, root, value):

        if root is None:
            return root
        
        if value < root.value:
            root.left = self.deleteTreeNode(root.left, value)
        elif value > root.value:
            root.right = self.deleteTreeNode(root.right, value)
        elif root.value == value:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            elif root.left != None and root.right != None:
                inorderSuccessor = self.getInorderSuccessor(root.right)
                root.value = inorderSuccessor.value
                self.deleteTreeNode(root.right, inorderSuccessor.value)
        return root

    def inorderTraversal(self, root):

        if root is None:
            return
        self.inorderTraversal(root.left)
        print(root.value)
        self.inorderTraversal(root.right)

    def getInorderTraversal(self, root):
        if root is None:
            return []

        return [root.value] + self.getInorderTraversal(root.left)

    def getBstIterator(self, root):
        self.stack = self.getInorderTraversal(root)
    
    def preorderTraversal(self, root):

        if root is None:
            return
        print(root.value)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def postOrderTraversal(self, root):

        if root is None:
            return

        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.value)

    def searchBST(self, root, val):
        if root:
            if root.value == val:
                return root
            elif val < root.value:
                return self.searchBST(root.left, val)
            elif val > root.value:
                return self.searchBST(root.right,val)
        return None

    def fillStack(self,root):
        if root is None:
            return []
        return self.fillStack(root.left) + [root.val] + self.fillStack(root.right)
    
                
    def next(self) -> int:
        """
        @return the next smallest number
        """

        minNode = self.stack.pop()
        self.stack += self.getInorderTraversal(minNode.right)
        return minNode.val
        

    # def hasNext(self) -> bool:
    #     """
    #     @return whether we have a next smallest number
    #     """
        
    #     return len(stack) > 0

bst = BinarySearchTree(50)
bst.insertExpensive(30, bst.root)
bst.insertExpensive(20, bst.root)
bst.insertExpensive(40, bst.root)
bst.insertExpensive(70, bst.root)
bst.insertExpensive(60, bst.root)
bst.insertExpensive(80, bst.root)
print(bst.getInorderTraversal(bst.root))
bst.getBstIterator(bst.root)
print(bst.next())
# bst.inorderTraversal(bst.root)
# bst.deleteTreeNode(bst.root, 20)
# bst.deleteTreeNode(bst.root, 20)
# bst.deleteTreeNode(bst.root, 50)
# bst.inorderTraversal(bst.root)
# bst.searchBST(bst.root, 20)
