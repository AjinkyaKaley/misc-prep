class Solution:

    def largestBSTSubtree(self, root):

        if not root:
            return (True, 0, float("inf"), float("-inf"))

        isLBst, Lsize, Lmin, Lmax  = self.largestBSTSubtree(root.left)
        isRBst, Rsize, Rmin, Rmax = self.largestBSTSubtree(root.right)

        if isLBst and isRBst and Lmax < root.val < Rmin:
            Lmin = Lmin if root.left else root.val
            Rmax = Rmax if root.right else root.val
            return (True, Lsize + Rsize + 1, Lmin, Rmax)
        
        return (False, max(Lsize, Rsize), float("inf"), float("-inf"))