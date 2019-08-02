class Solution:

    # def partition(self, nums, low, high):
    #     pivot = nums[high]
    #     low = low
    #     for j in range(low, high):
    #         if nums[j] > pivot:
    #             nums[j], nums[low] = nums[low], nums[j]
    #             low += 1
    #     nums[high], nums[low] = nums[low], nums[high]
    #     return low

    def partition(self, nums, left, right):
        pivot = nums[right]  # pick the last one as pivot
        i = left
        for j in range(left, right):  # left to right -1
            if nums[j] > pivot:  # the larger elements are in left side
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        # swap the i and the last element
        nums[right], nums[i] = nums[i], nums[right]
        return i
    def kthLarget(self, nums, low,high,k):
        low = 0
        high = len(nums) - 1
        p_pos = self.partition(nums, low, high)
        if p_pos == k - 1:
            return nums[p_pos]
        elif p_pos >= k:
            return self.kthLarget(nums, low, p_pos - 1, k)
        return self.kthLarget(nums, p_pos + 1, high, k)
    

q = Solution()
_data = [3, 2, 1, 5, 6, 4]
q.kthLarget(_data, 0, len(_data) - 1, 2)
print(_data)
