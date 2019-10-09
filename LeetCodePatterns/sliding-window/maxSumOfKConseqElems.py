class Solution:
    def kSumBruteForce(self, nums, k):
        n = len(nums)
        res = float("-inf")
        for i in range(n - k + 1):
            curr_sum = 0
            for j in range(k):
                curr_sum += nums[i + j]
            res = max(res, curr_sum)
        return res

    def kSumSlidingWidow(self, nums, k):
        n = len(nums)
        res = float("-inf")
        curr_sum=0
        for i in range(k):
            curr_sum += nums[i]
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            res = max(res, curr_sum)
        return res

sln = Solution()
print(sln.kSumSlidingWidow([100, 200, 100, 400, 500, 2, 600], k=5))

