# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None


class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Solution:

    def maxPathFromRoot(self, root):
        self.maxSum = 0
        def helper(root, currentSum):
            if root:
                if root.left == None and root.right == None:
                    currentTotal = currentSum + root.val
                    print(currentTotal)
                    if self.maxSum < currentTotal:
                        self.maxSum = currentTotal

                helper(root.left, currentSum+root.val)
                helper(root.right, currentSum + root.val)

        helper(root,0)
        return self.maxSum

    # def maxPathSum(self, root):
    #     self.result = 0
    #     def helper(root):
    #         if root:
    #             self.maxPathSum(root.left)
    #             self.maxPathSum(root.right)
    #             val = self.maxPathFromRoot(root)
    #             # valR = self.maxPathFromRoot(root.right)

    #             if val > self.result:
    #                 self.result = val

    #     helper(root)
    #     return self.result

# Python program to find maximumpath sum between two leaves
# of a binary tree


    # A binary tree node


    # Utility function to find maximum sum between any
    # two leaves. This function calculates two values:
    # 1) Maximum path sum between two leaves which are stored
    # in res
    # 2) The maximum root to leaf path sum which is returned
    # If one side of root is empty, then it returns INT_MIN


    def maxPathSumUtil(self,root, res):

        # Base Case
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        # Find maximumsum in left and righ subtree. Also
        # find maximum root to leaf sums in left and righ
        # subtrees ans store them in ls and rs
        ls = self.maxPathSumUtil(root.left, res)
        rs = self.maxPathSumUtil(root.right, res)

        # If both left and right children exist
        if root.left is not None and root.right is not None:

            # update result if needed
            res[0] = max(res[0], ls + rs + root.data)

            # Return maximum possible value for root being
            # on one side
            return max(ls, rs) + root.data

        # If any of the two children is empty, return
        # root sum for root being on one side
        if root.left is None:
            return rs + root.data
        else:
            return ls + root.data

    # The main function which returns sum of the maximum
    # sum path betwee ntwo leaves. THis function mainly
    # uses maxPathSumUtil()

    def maxPathSum(self, root):
        INT_MIN = -2**32
        res = [INT_MIN]
        self.maxPathSumUtil(root, res)
        return res[0]


    # Driver program to test above function
root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)


sln = Solution()

print ("Max pathSum of the given binary tree is", sln.maxPathSum(root))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(21)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# root.right.right.left = TreeNode(8)

# print(sln.maxPathSum(root))
