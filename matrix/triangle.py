class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        minLen = [] + triangle[n - 1]

        for layer in range(n-2, -1, -1):
            for i in range(layer + 1):
                minLen[i] = min(minLen[i], minLen[i+1]) + triangle[layer][i]

        return sum(minLen)

sln = Solution()
sln.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
])
