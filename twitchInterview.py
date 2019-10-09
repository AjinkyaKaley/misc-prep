# > 1 + 2 + 3 + 4 + 5 + 6 - 7 - 8 + 9
# > 1 + 2 + 3 + 4 + 5 - 6 + 7 + 8 - 9
# > 1 + 2 + 3 - 4 - 5 - 6 + 7 + 8 + 9
# > 1 + 2 - 3 + 4 - 5 + 6 - 7 + 8 + 9
# > 1 + 2 - 3 - 4 + 5 + 6 + 7 - 8 + 9
# > 1 - 2 + 3 + 4 + 5 - 6 - 7 + 8 + 9
# > 1 - 2 + 3 + 4 - 5 + 6 + 7 - 8 + 9
# > 1 - 2 + 3 - 4 + 5 + 6 + 7 + 8 - 9
# > 1 - 2 - 3 - 4 + 5 - 6 + 7 + 8 + 9

[1, 2, 3, 4, 5, 6, -7, -8, 9]
[1, 2, 3, 4, 5, -6, 7, 8, -9]
[1, 2, 3, -4, -5, -6, 7, 8, 9]
[1, 2, -3, 4, -5, 6, -7, 8, 9]
[1, 2, -3, -4, 5, 6, 7, -8, 9]
[1, -2, 3, 4, 5, -6, -7, 8, 9]
[1, -2, 3, 4, -5, 6, 7, -8, 9]
[1, -2, 3, -4, 5, 6, 7, 8, -9]
[1, -2, -3, -4, 5, -6, 7, 8, 9]
[-1, 2, 3, 4, 5, -6, 7, -8, 9]
[-1, 2, 3, 4, -5, 6, 7, 8, -9]
[-1, 2, -3, 4, -5, -6, 7, 8, 9]
[-1, 2, -3, -4, 5, 6, -7, 8, 9]
[-1, -2, 3, 4, -5, 6, -7, 8, 9]
[-1, -2, 3, -4, 5, 6, 7, -8, 9]
[-1, -2, -3, 4, 5, 6, 7, 8, -9]
[-1, -2, -3, -4, -5, 6, 7, 8, 9]
#  Write a function that, given an ordered array of positive integers and a target number, outputs all the ways to combine ALL the numbers,
# in order, with one of +, or - between them , such that they combine to sum to the target.

class Solution:
    def sum_equals_target(self, nums, target, curr_sum, curr_iter_result):
        
        if curr_sum == target and not nums:
            _sum = sum(curr_iter_result)
            _res = ''.join(','.join(str(v) for v in curr_iter_result))
            print(_res + " " + str(_sum))
            return
        elif curr_sum != target and not nums:
            return

        self.sum_equals_target(nums[1:], target, curr_sum + nums[0], curr_iter_result + [nums[0]]) or \
        self.sum_equals_target(nums[1:], target, curr_sum - nums[0], curr_iter_result + [-nums[0]])

sln = Solution()
sln.sum_equals_target([1, 2, 3, 4, 5, 6, 7, 8, 9], 15, 0, [])
