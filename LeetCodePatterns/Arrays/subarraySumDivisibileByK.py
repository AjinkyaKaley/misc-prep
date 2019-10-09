#https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/310767/(Python)-Concise-Explanation-and-Proof
#https://www.geeksforgeeks.org/count-the-number-of-pairs-i-j-such-that-either-arri-is-divisible-by-arrj-or-arrj-is-divisible-by-arri/


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
#         count = 0
#         aux = [0] * (len(nums) + 1)
#         for i in range(1, len(aux)):
#             aux[i] = aux[i - 1] + nums[i - 1]

#         for left in range(len(nums)):
#             for right in range(left + 1, len(nums) + 1):
#                 _s = aux[right] - aux[left]
#                 if _s % k == 0:
#                     count +=1
#         return count

        d = {0: 1}
        ans = 0
        csum = 0

        for i in range(len(nums)):
            csum += nums[i]
            rem = csum % k
            if rem in d:
                ans += d[rem]
                d[rem] += 1
            else:
                d[rem] = 1
            # d[rem]+= 1
        return ans

sln = Solution()
sln.subarraysDivByK([4, 5, 0, -2, -3, 1], k=5)