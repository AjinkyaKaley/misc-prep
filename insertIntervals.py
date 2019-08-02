class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left = [i for i in intervals if i[1] < newInterval[0]]
        right = [i for i in intervals if i[0] > newInterval[1]]
        if left + right != intervals:
            newInterval[0] = min(newInterval[0], intervals[len(left)][0])
            newInterval[1] = max(newInterval[1], intervals[~len(right)][1])
        return left + [newInterval] + right

sln = Solution()
print(sln.insert([[1, 3], [6, 9]], [2, 5]))