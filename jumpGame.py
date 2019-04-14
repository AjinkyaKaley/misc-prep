class Solution:

    def jumpGame(self, nums):

        if len(nums) == 1:
            return True

        root = nums[0]
        while root != 0:
            if root < len(nums):
                retValu = self.jumpGame(nums[root:])
                if retValu:
                    return True
            root-=1
        return False

    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

sln = Solution()
print(sln.canJump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
            