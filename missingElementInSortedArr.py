class Solution:
    def missingElement(self, nums, k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        def missing(idx):
            return nums[idx] - nums[0] - idx

        n = len(nums)
        # If kth missing number is larger than
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        idx = 1
        # find idx such that
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1

        # kth missing number is larger than nums[idx - 1]
        # and smaller than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)

sln = Solution()
sln.missingElement([4,7,9,10],1)