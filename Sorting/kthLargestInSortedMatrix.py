class Solution:

    def kthLargest(self, matrix, k):
        import heapq
        pq = [(element, 0, idx) for idx, element in enumerate(matrix[0])]
        heapq.heapify(pq)
        result = 0
        while k != 0:
            result, row, col  = heapq.heappop(pq)
            if row + 1 < len(matrix):
                heapq.heappush(pq, (matrix[row + 1][col], row + 1, col))
            k -= 1
        return result

sln = Solution()
print(sln.kthLargest([
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], 2))
