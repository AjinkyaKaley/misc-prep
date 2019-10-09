# Python program for an efficient solution to check if
# a given array can represent Preorder traversal of
# a Binary Search Tree

class Solution:

    INT_MIN = -2**32


    def canRepresentBST(self, pre):

        # Create an empty stack
        s = []

        # Initialize current root as minimum possible value
        root = float("-inf")

        # Traverse given array
        for value in pre:
            #NOTE:value is equal to pre[i] according to the
            #given algo

            # If we find a node who is on the right side
            # and smaller than root, return False
            if value < root:
                return False

            # If value(pre[i]) is in right subtree of stack top,
            # Keep removing items smaller than value
            # and make the last removed items as new root
            while(len(s) > 0 and s[-1] < value):
                root = s.pop()

            # At this point either stack is empty or value
            # is smaller than root, push value
            s.append(value)

        return True

sln = Solution()
sln.canRepresentBST([50, 17, 9, 14, 12, 23, 19, 50, 76, 54, 72, 67])