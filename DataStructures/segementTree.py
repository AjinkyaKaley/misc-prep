class Node:
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def __init__(self, nums):
        def constructSegTree(nums, low, high):
            
            if low > high:
                return None

            if low == high:
                return Node(low, high, nums[low])
                
            mid = (low+high)//2
            root = Node(low, high)
            root.left = constructSegTree(nums, low, mid)
            root.right = constructSegTree(nums, mid + 1, high)
            # root.val = min(root.left.val, root.right.val)
            root.val = root.left.val + root.right.val
            return root

        self.root = constructSegTree(nums, 0, len(nums) - 1)
        

    def update(self, idx, val):
        def helper(idx, val, root):
            
            if root.start == root.end:
                root.val = val
                return val
            mid = (root.start + root.end) // 2
            if idx <= mid:
                helper(idx, val, root.left)
            else:
                helper(idx, val, root.right)
            root.val = root.left.val + root.right.val
            return root.val
        helper(idx,val,self.root)

    def sumRange(self, i, j):
        def helper(i, j, root):
            if root.start == i and root.end == j:
                return root.val
            mid = (root.start + root.end) // 2
            if j <= mid:
                return helper(i, j, root.left)
            if i > mid:
                return helper(i, j, root.right)
            return helper(i, mid, root.left) + helper(mid + 1, j, root.right)

        return helper(i, j, self.root)
        
    def printSegTree(self, root):
        if root:
            self.printSegTree(root.left)
            print(root.val)
            self.printSegTree(root.right)


test = [1, 3, 5]
sln = Solution(test)
# sln.update()
sln.printSegTree(sln.root)
# def helper(low, high, nums, pos, segTree):
#             if low == high:
#                 segTree[pos] = low
#                 return

#             mid = (low + high) // 2
#             helper(low, mid, nums, 2 * pos + 1, segTree)
#             helper(mid + 1, high, nums, 2 * pos + 2, segTree)
#             segTree[pos] = min(segTree[(2 * pos) + 1], segTree[(2 * pos) + 2])
