class Solution(object):

    # O(n^3)
    def subarraySumBruteForce(self, nums, k):
        count = 0
        for start in range(0, len(nums)):
            for end in range(start+1, len(nums)+1):
                _s = sum(nums[start:end])
                if _s == k:
                    count += 1
        return count

    def subarraySumBetter(self, nums, k):
        count = 0
        aux = [0] * (len(nums) + 1)
        for i in range(1, len(aux)):
            aux[i] = aux[i - 1] + nums[i - 1]
        
        for start in range(0, len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if aux[end] - aux[start] == k:
                    count += 1
                    
        return count

    def subarraySumOptimal(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(lambda: 0)
        lookup[0] = 1
        s = 0
        res = 0
        
        for i in range(len(nums)):
            s += nums[i]
            if s - k in lookup:
                res += lookup[s - k]
            lookup[s] += 1
        
        return res

sln = Solution()
sln.subarraySumOptimal([1, 2, 3, 2], 5)
sln.subarraySumBruteForce([1, 2, 3], 3)
sln.subarraySumBetter([1, 2, 3, 3], 5)
# [1, 1, 1]
# [0, 1, 2, 3]
