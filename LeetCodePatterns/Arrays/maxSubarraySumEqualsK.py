class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        curr_max = 0   # current record of max length
        cum_sum = 0    # cumulative sum so far
        idx_dict = {0: -1}  # initialize the dictionary

        for i, num in enumerate(nums):
            cum_sum += num
            diff = cum_sum - k
            if diff in idx_dict:
                curr_max = max(curr_max, i - idx_dict[diff])
            if cum_sum not in idx_dict:
            # only keep the oldest index to have the longest subarray
                idx_dict[cum_sum] = i
        return curr_max

sln = Solution()
sln.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3)
