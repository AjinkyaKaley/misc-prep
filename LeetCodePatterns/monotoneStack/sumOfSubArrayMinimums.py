class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left = [0] * len(A)
        right = [0] * len(A)
        stack_1 = []
        stack_2 = []
        n = len(A)

        for i in range(n):
            count = 1
            while stack_1 and stack_1[-1][0] > A[i]:
                _val, _count = stack_1.pop()
                count += _count
            left[i] = count
            stack_1.append((A[i], count))
            
        for idx in range(n)[::-1]:
            count = 1
            while stack_2 and stack_2[-1][0] >= A[idx]:
                _val, _count = stack_2.pop()
                count += _count
            right[idx] = count
            stack_2.append((A[idx], count))
        mod = 10**9 + 7
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod


sln = Solution()
print(sln.sumSubarrayMins([3, 1, 2, 4]))
